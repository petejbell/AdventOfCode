# Day 5 challenge for me

with open('hard.txt') as f:
    grid = [line.rstrip() for line in f]
    grid = grid[:8]
    ins = [line for line in f]
    ins = ins[10:]
    print(grid)

'''
with open('hard.txt', 'r') as f:
    ins = f.readlines()
    for line in ins:
        line.strip()
    ins = ins[:10]
    print(ins.strip())
    #for line in range(:10):
    #    print(ins[line].strip())
'''    