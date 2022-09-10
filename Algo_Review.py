# get moving average 
class MovingAverage(object):
    def __init__(self,size):
        self.size = size 
        self.q = deque() # use the deque structure 
        self.sum = 0 
    
    def next(self,val):
        self.q.append(val)
        self.sum += val
        if len(self.q) <= self.size:
            pass 
        else:
            self.sum -= self.q.popleft()
        # the initial value isn't as big as size yet, therefore usiing len(self.q)
        return self.sum()/len(self.q)









    