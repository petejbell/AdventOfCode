# AoC Day 2.1

max_red = 12
max_green = 13
max_blue = 14
sum_IDs = 0

with open('2023/Day02/input.txt', 'r') as f:
    for game in f:
        possible = True
        game = game[4:]
        gamenumber = int(game.split(':')[0].strip())
        game = game.split(': ')[1].strip().split('; ')
        for hand in game:
            cubes = hand.split(', ')
            for colour in cubes:
                if possible:
                    cube_count = int(colour.split(' ')[0])
                    cube_col = colour.split(' ')[1]                    
                    if cube_count > max_blue and cube_col == 'blue':
                        possible = False
                    elif cube_count > max_green and cube_col == 'green':
                        possible = False                       
                    elif cube_count > max_red and cube_col == 'red':
                        possible = False
        if possible:
            sum_IDs += gamenumber            
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