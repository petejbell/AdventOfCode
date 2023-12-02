from stack import *
stacks = []
# Lovely hard-coded input - needs reading from file
content = ['TPZCSLQN', 'LPTVHCG', 'DCZF', 'GWTDLMVC', 'PWC', 'PFJDCTSZ', 'VWGBD', 'NJSQHW', 'RCQFSLV']

for i in range(len(content)):
    stacks.append(Stack())
    for letter in content[i]:
        stacks[i].push(letter)
      
with open('input.txt') as f:
    instructions = [line.rstrip() for line in f]
    for instruction in instructions:
        if len(instruction) < 22 and len(instruction) > 0: # ignores grid
            instruction = instruction[5:]
            if len(instruction) > 13: # takes care of double digit instructions
                moves = int(instruction[0:2])
                movefrom = int(instruction[8])
                moveto = int(instruction[13])
                for i in range(moves):
                    copy = stacks[movefrom-1].gettop()
                    stacks[moveto-1].push(copy)
                    stacks[movefrom-1].pop()
            else:
                moves = int(instruction[0])
                movefrom = int(instruction[7])
                moveto = int(instruction[12])
                for i in range(moves):
                    copy = stacks[movefrom-1].gettop()
                    stacks[moveto-1].push(copy)
                    stacks[movefrom-1].pop()
for stack in stacks:
    stack.peek() # Output the top crate on each stack
