from stack import *
    
stacks = []
stack1 = Stack()
stack2 = Stack()
stack3 = Stack()
hold = Stack()

stacks.append(stack1)
stacks.append(stack2)
stacks.append(stack3)


text1 = 'ZN'
text2 = 'MCD'
text3 = 'P'

for each in text1:
    stack1.push(each)
for each in text2:
    stack2.push(each)
for each in text3:
    stack3.push(each)

with open('test.txt') as f:
    instructions = f.readlines()
    for instruction in instructions:
        instruction = instruction.strip()
        if len(instruction) > 0: # ignores grid
            instruction = instruction[5:]
            if len(instruction) > 13: # takes care of double digit instructions
                moves = int(instruction[0:2])
                movefrom = int(instruction[8])-1
                moveto = int(instruction[13])-1
                for i in range(moves):
                    hold.push(stacks[movefrom].gettop())
                    stacks[movefrom].pop()
                for i in range(moves):
                    stacks[moveto].push(hold.gettop())
                    hold.pop()
            else:
                moves = int(instruction[0])
                movefrom = int(instruction[7])-1
                moveto = int(instruction[12])-1
                for i in range(moves):
                    hold.push(stacks[movefrom].gettop())
                    stacks[movefrom].pop()
                for i in range(moves):
                    stacks[moveto].push(hold.gettop())
                    hold.pop()

for stack in stacks:
    print(stack.stack)
crates = 0
for stack in stacks:
    stack.peek() # Output the top crate on each stack
    crates += stack.qty() # Have I still got all the crates?
print(crates)
