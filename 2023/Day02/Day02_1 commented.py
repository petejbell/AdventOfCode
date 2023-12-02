
# AoC Day 2.1

max_red = 12
max_green = 13
max_blue = 14
sum_IDs = 0
with open('2023/Day02/test.txt', 'r') as f:
    for game in f:
        possible = True

        game = game[4:]
        gamenumber = int(game.split(':')[0].strip())  # GOOD
        games = game.split(': ')[1].strip()

        #print('GAME: ', gamenumber, '-----')
        #print(games)
        sets_of_hands = games.split('; ')
        #print(sets_of_cubes)
        
        
        for hand in sets_of_hands:
            #print('------NEW HAND------')        
            cubes = hand.split(', ')
            #print(cubes)

            for cube in cubes:
                if possible:
                    cube_count = int(cube.split(' ')[0])
                    cube_col = cube.split(' ')[1]
                    
                    #print(cube_count, cube_col)
                    
                    if cube_count > max_blue and cube_col == 'blue':
                        possible = False
                        #print('impossible \n')
                        
                    elif cube_count > max_green and cube_col == 'green':
                        possible = False
                        #print('impossible')
                        
                    elif cube_count > max_green and cube_col == 'red':
                        possible = False
                        #print('impossible')
        
        if possible:
            sum_IDs += gamenumber
            print('GAME',gamenumber,'POSSIBLE.','Sum of IDs:', sum_IDs)
        else:
            print('GAME',gamenumber,'XXXXXXXXXXXXXXXXXXXXXXX')

        #print(gamenumber, possible)                    
    print(sum_IDs)




'''
with open('2023/Day02/input.txt', 'r') as f:
    for game in f:
        first_digit = ''
        last_digit = 0

        for each in line:
            if each.isdigit():
                first_digit = (each)
                break
        # print (first_digit)

        while last_digit < 1:
            for each in line:
                if each.isdigit():
                    last_digit = int(each)
        # print (last_digit)

        line_calvalue = str(first_digit)+str(last_digit)
        # print (int(line_calvalue))
        total_cal += int(line_calvalue)

    print(total_cal)
'''