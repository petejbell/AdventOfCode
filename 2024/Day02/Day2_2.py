# AoC Day 2.2

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

def validate_with_one_removal(numbers):
    # Check if the original list itself satisfies the conditions
    if (is_growing(numbers) or is_shrinking(numbers)) and difference_within_three(numbers):
        print("The original list passes all conditions.")
        return True

    # Iterate through the list, removing one item at a time
    for i in range(len(numbers)):
        # Create a modified list excluding the current item
        modified_list = numbers[:i] + numbers[i+1:]
        
        # Check all three functions with the modified list
        if (is_growing(modified_list) or is_shrinking(modified_list)) and difference_within_three(modified_list):
            print(f"List passes with the removal of item at index {i}: {numbers[i]}")
            return True

    # If no modified list satisfies the conditions
    print("No combination passes all checks.")
    return False


with open('2024/Day02/input.txt', 'r') as f:
    safe_nums = 0
    for line in f:
        numbers = [int(num) for num in line.split()]
        print(f"Checking line: {numbers}")
        if validate_with_one_removal(numbers):
            safe_nums += 1
print(safe_nums)