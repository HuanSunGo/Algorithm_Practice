# Implement a queue using two stacks
"""
enqueue: put the number in to the stack s1
dequeue: use s2 to simulate the exit of the queue, pop the nubers into the s2 
wathch the animation for understanding
"""
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

    


