def check_ignition(b_grid, f_grid, h_grid, i_threshold, w_direction, i, j):
    m = len(b_grid)
    wd = {}
    adjacent = []
    factor = 0 
    if not b_grid[i][j]:
        if f_grid[i][j] > 0:
            
            # scenario 1: without wind 
            if w_direction is None:
                for (coord1, coord2) in [(i + 1, j), (i - 1, j), (i, j + 1), 
                                         (i, j - 1), (i + 1, j + 1), 
                                         (i + 1, j - 1), (i - 1, j - 1), 
                                         (i - 1, j + 1)]:
                    if 0 <= coord1 < m and 0 <= coord2 < m:
                        adjacent.append((coord1, coord2))
                for ((coord1, coord2)) in adjacent:
                    if b_grid[coord1][coord2] is True:
                        if h_grid[coord1][coord2] > h_grid[i][j]:
                            factor += 0.5
                        elif h_grid[coord1][coord2] == h_grid[i][j]:
                            factor += 1
                        elif h_grid[coord1][coord2] < h_grid[i][j]:
                            factor += 2
                return factor >= i_threshold
            
            # scenario 2: with wind
            if w_direction is not None:
                for (coord1, coord2) in [(i + 1, j), (i - 1, j), (i, j + 1), 
                                          (i, j - 1), (i + 1, j + 1), 
                                           (i + 1, j - 1), (i - 1, j - 1), 
                                            (i - 1, j + 1)]:
                    if 0 <= coord1 < m and 0 <= coord2 < m:
                        adjacent.append((coord1, coord2))
                wd['N'] = [(i, j + 2), (i - 1, j + 2), (i + 1, j + 2)]
                wd['E'] = [(i + 2, j), (i + 2, j - 1), (i + 2, j + 1)]
                wd['S'] = [(i, j - 2), (i - 1, j - 2), (i + 1, j - 2)]
                wd['W'] = [(i - 2, j), (i - 2, j - 1), (i - 2, j + 1)]
                wd['NE'] = [(i + 2, j + 2), (i + 2, j + 1), (i + 1, j + 2)]
                wd['NW'] = [(i - 2, j + 2), (i - 2, j + 1), (i - 1, j + 2)]
                wd['SE'] = [(i + 2, j - 2), (i + 2, j - 1), (i + 1, j - 2)]
                wd['SW'] = [(i - 2, j - 2), (i - 2, j - 1), (i - 1, j - 2)]
                for values in wd.values():
                    for (coord1, coord2) in values:
                        if 0 <= coord1 < m and 0 <= coord2 < m:
                            adjacent.append((coord1, coord2))
                            
    # adjacent's contribution to the ignition factor of the cell
                for ((coord1, coord2)) in adjacent:
                    if b_grid[coord1][coord2] is True:
                        if h_grid[coord1][coord2] > h_grid[i][j]:
                            factor += 0.5
                        elif h_grid[coord1][coord2] == h_grid[i][j]:
                            factor += 1
                        elif h_grid[coord1][coord2] < h_grid[i][j]:
                            factor += 2
                return factor >= i_threshold
        else:
            return False
    else:
        return False

   