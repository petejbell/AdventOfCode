# AoC Day 1.1

count = 0
left_nums = []
right_nums = []

with open('2024/Day01/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        left_nums.append(int(line[0:5]))
        right_nums.append(int(line[-5:]))
    for item in left_nums:
        count += item * right_nums.count(item)
print(count)
