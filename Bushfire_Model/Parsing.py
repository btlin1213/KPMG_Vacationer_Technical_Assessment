import csv

def parse_scenario(filename):
    ''' parses a given file into format as described in question''' 
    
    keys = ['f_grid', 'h_grid', 'i_threshold', 'w_direction', 'burn_seeds']
    answer = {}
    prelines = []
    lines = []
    
# prelines = list of str(lines) in lists (nested list), height = first number
    with open(filename, 'r') as csv_file:
        data = csv.reader(csv_file)
        prelines = [line for line in data]
        height = int(prelines[0][0])
        coord1 = int(prelines[-1][0]) 
        coord2 = int(prelines[-1][1])
 
    # dimension is positive
        if height < 0:
            return 
    # ignition is positive smaller than 8 
        elif int(prelines[-3][0]) <= 0 or int(prelines[-3][0]) > 8:
            return 
    # wind direction is valid
        elif prelines[-2][0] not in ['N', 'S', 'E', 'W', 'SE', 'SW', 
                                     'NE', 'NW']:
            return
    # coordinates of burning cell is on landscape and is non-zero 
        elif coord1 not in range(0, height) or coord2 not in range(0, height) \
         or int(prelines[1 + coord1][coord2]) == 0:
            return 
        
# lines = list of integer lists as required in answer
    i = 1
    while i in range(1, 2 * height + 2):
        line1 = prelines[i]
        line1 = list(map(int, line1))
        lines.append(line1)
        i += 1
        
    answer[keys[0]] = lines[0:height]
    answer[keys[1]] = lines[height: height + height]
    answer[keys[2]] = lines[height + height][0]
    answer[keys[3]] = prelines[2 * height + 2][0]
    answer[keys[4]] = [tuple((int(prelines[2 * height + 3][0]), 
                                int(prelines[2 * height + 3][1])))]
    return answer
    
 
   
    
    
            
           
        
        
        
   