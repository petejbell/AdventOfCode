def full():
    if top == maxsize - 1:
        return True
    else:
        return False


def empty():
    if top == -1:
        return True
    else:
        return False


def push(data):
    global top
    #add your push code here
    if full():
        print('stack overflow')
    else:
        top += 1
        stack[top] = data


def pop():
    global top
    #add your pop code here
    if empty():
        print('stack underflow')
    else:
        stack[top] = ''
        top -= 1


def peek():
    return stack[top]


stack = []
top = -1  #pointer

maxsize = 10
for i in range(0, maxsize):
    stack.append('')

push('cat')
print(stack)
push('dog')
print(stack)
push('donkey')
print(stack)
pop()
print(stack)
