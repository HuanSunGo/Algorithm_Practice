"""
Queue
--------
Queue: enqueue --> put one element into our queue
Dequeue: dequeue --> take one element out from our queue
FIFO

Stack
-------
push, pop, FILO
Implementation in Python: list
"""


# Implement a queue using two stacks
"""
enqueue: put the number in to the stack s1
dequeue: use s2 to simulate the exit of the queue, pop the nubers into the s2 
wathch the animation for understanding
"""
from operator import is_


class Queue: 
    def __init__(self):
        self.s1 = [] # stack in python
        self.s2 = []
    
    def enqueue(self,x): 
        """
        TC: O(1)
        """
        self.s1.append(x)

    
    def dequeue(self):
        """
        TC: worst case --> O(n), amortized --> O(1)
        """
        if not self.s2: 
            while self.s1: # if s1 still have elements
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    
    def is_empty(self):
        # return true only when s1 and s2 are both not empty 
        return not self.s2 and not self.s2 
    
    def size(self):
        return len(self.s1) + len(self.s2)
          
# implement a stack with MAX API
class StackMax: 
    """
    Trade space for time.
    stack (x, x_max), x_max: max value from bottom of stack to x 
    stack = []
    stack = [(1,1)]
    stack = [(1,1),(2,2)]
    stack = [(1,1),(2,2),(0,2)]
    stack = [(1,1),(2,2),(0,2),(3,3)]
    stack = [(1,1),(2,2),(0,2),(3,3),(-1,3)]
    """
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0 
    
    def push(self,x):
        if self.is_empty():
            self.stack.append((x,x))
        else: 
            x_max = self.stack[-1][1] # compare the previous one in the tuple, and don't need to compare them all 
            self.stack.append((x,max(x,x_max)))

    def pop(self):
        item = self.stack.pop()
        return item[0]

    def max(self):
        return self.stack[-1][1]
        
    


