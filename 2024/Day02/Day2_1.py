# AoC Day 2.1

safe_nums = 0


def is_growing(numbers):
    return numbers == sorted(numbers) and len(set(numbers)) == len(numbers)


def is_shrinking(numbers):
    return numbers == sorted(numbers, reverse=True) and len(set(numbers)) == len(numbers)


def difference_within_three(numbers):
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i] - numbers[i + 1])  
        if difference > 3:
            return False
    return True


with open('2024/Day02/input.txt', 'r') as f:
    for line in f:
        numbers = [int(num) for num in line.split()]
        if (is_growing(numbers) or is_shrinking(numbers)) and difference_within_three(numbers):
            safe_nums += 1
    print(safe_nums)
