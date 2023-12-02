# AoC Day 1.1

with open('2023/Day01/stuff.txt', 'r') as f:
    total_cal = 0
    for line in f:
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
