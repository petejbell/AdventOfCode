# Advent of Code Day 2_1

total = 0

def gameresult(opp, you):
    score = 0
    
    if you == 'X':
        score += 1
        if opp == 'A':
            score += 3
        if opp == 'B':
            score += 0
        if opp == 'C':
            score += 6
            
    elif you == 'Y':
        score += 2
        if opp == 'A':
            score += 6
        if opp == 'B':
            score += 3
        if opp == 'C':
            score += 0
            
    elif you == 'Z':
        score += 3
        if opp == 'A':
            score += 0
        if opp == 'B':
            score += 6
        if opp == 'C':
            score += 3

    return score

with open('input.txt', 'r') as f:
    for game in f:
        total += gameresult(game[0],game[2])
print(total)