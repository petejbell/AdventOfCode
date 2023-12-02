# AoC Day 10
cycles = 0
reg = 1
lines = []
pxl = 0
crt = ''
    
with open('day10.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lines.append(line)
    lines.reverse()

def draw():
    global crt
    global pxl
    if cycles % 40 == 0:
        pxl = 0
        print(crt)
        crt = ''
    else:
        pxl += 1
    if pxl == reg or pxl == reg-1 or pxl == reg+1:
        crt += '#'
    else:
        crt += '.'

draw()
while len(lines)>0:
    cycles += 1
    inst = lines.pop()
    draw()
    if inst[0] == 'a':
        cycles += 1
        if inst[0:5] == 'addx ':
            reg += int(inst[5:])
        draw()