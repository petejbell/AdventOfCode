# Advent Of Code Day 1

with open("CALORIES.txt", "r") as f:

    elves = []
    elf_calories = 0

    for line in f:
        if line != '\n':
            elf_calories += int(line)
        else:
            elves.append(elf_calories)
            elf_calories = 0
            
        
    print('Elf',elves.index(max(elves)),'is carrying',str(max(elves)),'calories')