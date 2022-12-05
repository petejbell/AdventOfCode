from typing import List

class Stack():
    
    def __init__(self):
        self.pointer = -1
        self.stack = [] # type: List[str]
    
    def push(self, item):
        self.stack.append(item)
        self.pointer += 1
        #self.draw_stack()
    
    def pop(self):
        #check for underflow
        if self.pointer == -1:
            print('***stack underflow***')
        else:
            self.stack.remove(self.stack[self.pointer])
            self.pointer -= 1
    #       print(self.stack[-1])
    #  self.draw_stack()
    #remove item on stack pointed to by pointer
    #move the pointer down
    #self.draw_stack()
  
    
    def draw_stack(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])
  
    
    def peek(self):
        #output the top item of the stack
        print(self.stack[self.pointer])
    
    def gettop(self):
        #output the top item of the stack
        return(self.stack[self.pointer])
