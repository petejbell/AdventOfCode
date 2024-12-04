# AoC Day 1.1

distances = 0
left_nums = []
right_nums = []

with open('2024/Day01/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        left_nums.append(int(line[0:5]))
        right_nums.append(int(line[-5:]))
    while len(left_nums) > 0:
        smallest_left = min(left_nums)
        smallest_right = min(right_nums)
        distances += max(smallest_right, smallest_left) - min(smallest_right, smallest_left)
        left_nums.remove(smallest_left)
        right_nums.remove(smallest_right)
print(distances)
