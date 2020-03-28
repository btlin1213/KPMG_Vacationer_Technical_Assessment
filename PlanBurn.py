from hidden import check_ignition, update_state, run_model
def plan_burn(f_grid, h_grid, i_threshold, town_cell):
    ''' return list of highest score prescribed burn cells ''' 
    m = len(f_grid)
    x = town_cell[0]
    y = town_cell[1]
    coordinates = [(i, j) for i in range(m) for j in range(m)]
    lst = []
    lst2 = []
    final_states = {}
    fail_count = {}
    
    # produce dict with final fuel state (value) for each 
    # non-zero and non-town cell as prescribed burn cell (key)
    for (i, j) in coordinates:
        if (i, j) != town_cell and f_grid[i][j] > 0:
            final_states[(i, j)] = run_model(f_grid, h_grid, 
                                             2 * i_threshold, 
                                             None, [(i, j)])[0]
            
    # if town cell burned, delete that key-value pair
    for cell, states in final_states.items():
        if states[x][y] == 0:
            del final_states[cell]
    
    # for each cell in final states dict as burn_seed, produce 9 wind scenarios
    # if town cell is burned, fail + 1 
    for cell, state in final_states.items():
        fail = 0 
        burn_seeds = [(i, j) for (i, j) in coordinates if 
                       (i, j) != town_cell and state[i][j] > 0]
        for (i, j) in burn_seeds:
            for wind in ['N', 'S', 'E', 'W', 'SE', 'SW', 'NE', 'NW', None]:
                if run_model(state, h_grid, i_threshold, 
                                    wind, [(i, j)])[0][x][y] == 0:
                    fail += 1
        fail_count[cell] = fail
    
    # sort the prescribed burn cell by total of fail
    for pres_cell, total_fail in fail_count.items():
        lst2.append(total_fail)
        lst.append((total_fail, pres_cell))
    
    # return sorted list of prescribed cell with lowest number of fail 
    answer = [pres_cell for (total_fail, 
                             pres_cell) in lst if total_fail == min(lst2)]
    return sorted(answer)