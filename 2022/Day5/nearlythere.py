from stack import *
    
stacks = []
stack1 = Stack()
stack2 = Stack()
stack3 = Stack()
stack4 = Stack()
stack5 = Stack()
stack6 = Stack()
stack7 = Stack()
stack8 = Stack()
stack9 = Stack()

stacks.append(stack1)
stacks.append(stack2)
stacks.append(stack3)
stacks.append(stack4)
stacks.append(stack5)
stacks.append(stack6)
stacks.append(stack7)
stacks.append(stack8)
stacks.append(stack9)

text1 = 'TPZCSLQN'
text2 = 'LPTVHCG'
text3 = 'DCZF'
text4 = 'GWTDLMVC'
text5 = 'PWC'
text6 = 'PFJDCTSZ'
text7 = 'VWGBD'
text8 = 'NJSQHW'
text9 = 'RCQFSLV'

for each in text1:
    stack1.push(each)
for each in text2:
    stack2.push(each)
for each in text3:
    stack3.push(each)
for each in text4:
    stack4.push(each)
for each in text5:
    stack5.push(each)
for each in text6:
    stack6.push(each)
for each in text7:
    stack7.push(each)
for each in text8:
    stack8.push(each)
for each in text9:
    stack9.push(each)
   
with open('input.txt') as f:
    instructions = f.readlines()
    for instruction in instructions:
        instruction = instruction.strip()
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
for each in stacks:
    each.peek()      
                