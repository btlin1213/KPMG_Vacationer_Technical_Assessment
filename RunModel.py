
from reference import check_ignition

def create_b(m, seeds):
    ''' initialising b_grid ''' 
    # ans = list of lists of dimension same as f_grid, but all False. 
    ans = [[False] * m for dimension in range(m)]
    for (coord1, coord2) in seeds:
        ans[coord1][coord2] = True
    return ans          

def run_model(f_grid, h_grid, i_threshold, w_direction, burn_seeds):
    ''' return final fuel state of landscape and total cells burned ''' 
    
    m = len(f_grid)
    b = create_b(m, burn_seeds)
    f = f_grid 
    coordinates = [(i, j) for i in range(m) for j in range(m)]
    count = set()
    count.update(burn_seeds)

    # run model until b_grid is all False (no cell is burning) 
    while b != [[False] * m for dimension in range(m)]:
        catch_fire_cells = []
        burning_cells = []
        
        # classify each coordinate into a list from above 
        for (i, j) in coordinates:
            if b[i][j]:
                if (i, j) not in burning_cells:
                    burning_cells.append((i, j))
            if not b[i][j]:
                if check_ignition(b, f, h_grid, i_threshold, 
                                      w_direction, i, j):
                        catch_fire_cells.append((i, j))
        
        # burning cells fuel load -1 and evaluate to False if fuel = 0 after -1
        for (i, j) in burning_cells:
            if f[i][j] - 1 > 0:
                b[i][j] = True
            if f[i][j] -1 == 0:
                b[i][j] = False
            f[i][j] -= 1
        
        # cells that catch fire at t+1 evaluate to True
        # add to count of cells burned 
        for (i, j) in catch_fire_cells:
            b[i][j] = True
            count.add((i, j))
   
    return (f, len(count))
    
    