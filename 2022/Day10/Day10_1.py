# AoC Day 10
cycles = 0
reg = 1
lines = []
totsignal = 0
    
with open('day10.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lines.append(line)
    lines.reverse()

def chksig(x, r):    
    signal = 0
    if x == 20 or (x-20) % 40 == 0:
        signal = x*r
#        print('*'*50)
#        print(signal)
    return signal

while len(lines)>0:
    cycles += 1
#    print('cycle number',str(cycles),'starts')
    totsignal += chksig(cycles, reg)
    inst = lines.pop()
#     print(inst)
    if inst[0] == 'a':
        cycles += 1
        totsignal += chksig(cycles, reg)
        if inst[0:5] == 'addx ':
#            print('X +',str(int(inst[5:])),'=',str(reg+int(inst[5:])))
            reg += int(inst[5:])

print(totsignal)      








def execute():
    lines.push('pause')
    if inst[0:5] == 'addx ':
        print('X +',str(int(inst[5:])),'=',str(reg+int(inst[5:])))
        reg += int(inst[5:])
        
        
        
        
'''
else:
            print(int(inst.split()[1:-1]))
            reg += int(inst.split()[1:-1])
            print(reg)
            delay +=2
            
        
    else:
        execute()
        cycles += 1
      
 
        changeReg()
    sleep(1)
        

    for each in lines:
        if each[0] == 'n':
            delay += 1
        else:
            delay +=2
print(clock)
'''