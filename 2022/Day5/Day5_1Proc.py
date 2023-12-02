from stack import *
    
stacks = []
stack1 = 'TPZCSLQN'
stack2 = 'LPTVHCG'
stack3 = 'DCZF'
stack4 = 'GWTDLMVC'
stack5 = 'PWC'
stack6 = 'PFJDCTSZ'
stack7 = 'VWGBD'
stack8 = 'NJSQHW'
stack9 = 'RCQFSLV'

stacks.append(stack1)
stacks.append(stack2)
stacks.append(stack3)
stacks.append(stack4)
stacks.append(stack5)
stacks.append(stack6)
stacks.append(stack7)
stacks.append(stack8)
stacks.append(stack9)

# print(stacks[5][-1])

'''
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

'''


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
                    if len(stacks[movefrom-1]) > 0:
                        copy = stacks[movefrom-1][-1]
                        stacks[moveto-1] += copy
                        deletedlast = stacks[movefrom-1].rstrip(stacks[movefrom-1][-1])
                        stacks[movefrom-1] = deletedlast
            else:
                moves = int(instruction[0])
                movefrom = int(instruction[7])
                moveto = int(instruction[12])
                for i in range(moves):
                    if len(stacks[movefrom-1]) > 0:
                        copy = stacks[movefrom-1][-1]
                        stacks[moveto-1] += copy
                        deletedlast = stacks[movefrom-1].rstrip(stacks[movefrom-1][-1])
                        stacks[movefrom-1] = deletedlast
for each in stacks:
    #print(each)
    if each == '':
        print(stacks.index(each)+1)
    else:
        print(stacks.index(each)+1,each)