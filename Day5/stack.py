from typing import List

class Stack():
    
    def __init__(self):
        self.pointer = -1
        self.stack = [] # type: List[str]
    
    def push(self, item):
        self.stack.append(item)
        self.pointer += 1
    
    def pop(self):
        #check for underflow
        if self.pointer == -1:
            print('***stack underflow***')
        else:
            #return(self.stack[self.pointer])
            self.stack.remove(self.stack[self.pointer])
            self.pointer -= 1
  
    
    def draw_stack(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])
  
    
    def peek(self):
        #print the top item of the stack
        print(self.stack[self.pointer])
    
    def gettop(self):
        #get the top item of the stack
        return(self.stack[self.pointer])
    
    def qty(self):
        #get the number of crates in the stack
        return(len(self.stack))
