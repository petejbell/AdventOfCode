def letToNum(comp):
    this_comp = []
    for item in comp:
        for letter in item:
            if ord(letter) > 90:
                letter = ord(letter)-96
                this_comp.append(letter)
            else:
                letter = ord(letter)-38
                this_comp.append(letter)
    return(set(this_comp))
    this_comp = []

with open("day3.txt", "r") as sacks:
    total = 0
    for sack in sacks:
        comp1 = letToNum(sack[:len(sack)//2])
        comp2 = letToNum(sack[len(sack)//2:])
        a = (comp1 & comp2)
        for i in a:
            total += i
    print(total)