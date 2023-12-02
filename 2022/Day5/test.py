from stack import *
    
first = Stack()
second = Stack()
third = Stack()
fourth = Stack()
fifth = Stack()
sixth = Stack()
seventh = Stack()
eighth = Stack()
nineth = Stack()
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
    first.push(each)
for each in text2:
    second.push(each)
for each in text3:
    third.push(each)
for each in text4:
    fourth.push(each)
for each in text5:
    fifth.push(each)
for each in text6:
    sixth.push(each)
for each in text7:
    seventh.push(each)
for each in text8:
    eighth.push(each)
for each in text9:
    nineth.push(each)
      
def peekAll():
    first.peek()
    second.peek()
    third.peek()
    fourth.peek()
    fifth.peek()
    sixth.peek()
    seventh.peek()
    eighth.peek()
    nineth.peek()

peekAll()

with open('test.txt') as f:
    moves = f.readlines()
    print(moves)


'''
def menu(stack):
  choice = 0
  while choice !=9:
    print('1. Push crate')
    print('2. Push monkey')
    print('3. Pop')
    print('4. Peek')
    print('9. Exit')
    choice = int(input('What would you like to do?'))
    if choice == 1:
      mystack.push('crate')
    elif choice == 2:
      mystack.push('monkey')
    elif choice == 3: 
      mystack.pop()
    elif choice == 4:
      mystack.peek()
'''
# mystack = Stack()
# menu(mystack)
