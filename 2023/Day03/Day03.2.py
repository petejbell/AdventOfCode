# AoC Day 3.2

def find_partnumbers(grid, row, col):
    part_numbers = set()

    # Iterate through rows above and below the asterisk
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            # Skip the asterisk
            if r == row and c == col:
                continue

            # Check if the current cell contains a digit
            if grid[r][c].isdigit():
                current_number = grid[r][c]

                # Check right
                for i in range(1, 3):
                    if c + i < len(grid[0]) and grid[r][c + i].isdigit():
                        current_number += grid[r][c + i]
                    else:
                        break

                # Check left
                for i in range(1, 3):
                    if c - i >= 0 and grid[r][c - i].isdigit():
                        current_number = grid[r][c - i] + current_number
                    else:
                        break

                part_numbers.add(int(current_number))

    return list(part_numbers)

        


with open('2023/Day03/input.txt', 'r') as f:
    columns = 0
    rows = 0
    grid = []
    star = '*'
    sum_of_gear_ratios = 0
    lines = f.read().splitlines()
    for line in lines:
        rows += 1
        grid.append(line)
    for item in lines[0]:
        columns += 1

    for j in range(columns):
        for i in range(rows):
            pos = grid[j][i]
            if (pos) == star:
                #print('Line',j+1)
                to_multiply = find_partnumbers(grid, j, i)
                if (to_multiply is not None) and len(to_multiply) > 1:
                    #print(to_multiply)
                    product = 1
                    for gear in to_multiply:
                        product *= int(gear)
                    sum_of_gear_ratios += product
                    #print('SUM OF ALL RATIOS =',sum_of_gear_ratios)
    print('FINAL SUM OF ALL RATIOS =',sum_of_gear_ratios)
