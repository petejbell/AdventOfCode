# AoC Day 2.2

power = 0
with open('2023/Day02/input.txt', 'r') as f:
    for game in f:
        max_red = 0
        max_green = 0
        max_blue = 0
        game = game[4:]
        gamenumber = int(game.split(':')[0].strip())
        game = game.split(': ')[1].strip().split('; ')
        for hand in game:
            cubes = hand.split(', ')
            for colour in cubes:
                cube_count = int(colour.split(' ')[0])
                cube_col = colour.split(' ')[1]                    
                if cube_count > max_blue and cube_col == 'blue':
                    max_blue = cube_count
                elif cube_count > max_green and cube_col == 'green':
                    max_green = cube_count
                elif cube_count > max_red and cube_col == 'red':
                    max_red = cube_count
        power += max_blue * max_green * max_red            
print(power)