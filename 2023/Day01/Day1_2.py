# AoC Day 1.2

number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('2023/Day01/input.txt', 'r') as f:
    total_cal = 0
    count = 0
    for line in f:
        backwards = line[::-1]
        first_digit = ''
        last_digit = 0
        count += 1
        numbers = {}

        for i in number_dict:
            if i in line:
                numbers.update({line.find(i): number_dict.get(i)})

        for i in number_dict:
            ir = i[::-1]
            if ir in backwards:
                numbers.update(
                    {len(backwards)-backwards.find(ir)-1: number_dict.get(ir[::-1])})

        for n in line:
            if n.isdigit():
                first_digit = n
                numbers.update({line.find(n): int(n)})

        for n in backwards:
            if n.isdigit():
                numbers.update({len(backwards)-backwards.find(n)-1: int(n)})

        line_calvalue = str(numbers[min(numbers)]) + str(numbers[max(numbers)])
        #print(count, int(line_calvalue))
        total_cal += int(line_calvalue)

    print(total_cal)
