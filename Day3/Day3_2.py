def letToNum(sack):
    this_sack = []
    for letter in sack:
        if ord(letter) > 90:
            letter = ord(letter)-96
            this_sack.append(letter)
        else:
            letter = ord(letter)-38
            this_sack.append(letter)
    return(set(this_sack))
    this_sack = []

with open("day3.txt", "r") as f:
    sacks = f.readlines()    
    group = []
    total = 0
    while len(sacks)>0:
        while len(group) < 3:
            group.append(letToNum(sacks[0].strip()))
            del sacks[0]
        a = (group[0] & group[1] & group[2])
        for i in a:
            total += i
        group = []
print(total)