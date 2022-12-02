# Advent of Code Day 2_1

total = 0

def gameresult(opp, you):
    score = 0

    if you == 'X': # LOSE
        score += 0
        if opp == 'A':
            score += 3
        if opp == 'B':
            score += 1
        if opp == 'C':
            score += 2
            
    elif you == 'Y': # DRAW
        score += 3
        if opp == 'A':
            score += 1
        if opp == 'B':
            score += 2
        if opp == 'C':
            score += 3
            
    elif you == 'Z': # WIN
        score += 6
        if opp == 'A':
            score += 2
        if opp == 'B':
            score += 3
        if opp == 'C':
            score += 1
    return score

with open('input.txt', 'r') as f:
    for game in f:
        total += gameresult(game[0],game[2])
print(total)