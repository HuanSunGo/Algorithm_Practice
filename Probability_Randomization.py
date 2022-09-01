
""" 
Shuffling Algorithm
--------------------
random.random(): return random float number in [0,1) - uniformly distributed 
random.randint(x,y):return random int number in [x,y] - uniformly distributed 

Use index as the unique pointer
"""

def shuffle_deck(array):
    """
    TC: O(n)
    SC: O(1)
    """
    length = len(array)
    # put at the end of the array, and include the index 0(optional)
    for pos in range(length -1, -1, -1):
        random_number = random.randint(0,pos) 
        array[pos], array[random_number] = array[random_number], array[pos]
    return array 

"""
Reservoir Sampling
-------------------
Given an unlimited data flow, return one random number among all numbers read so far, 
such that the probability of returning any element read so far is 1/n.

Maintain two variables: counter and sample, so that don't need to store the uncertain large number of data 
"""

class Generator:
    
    def __init__(self ,k):
        self.sample = []
        self.count = 0 # the counter of elements read so far
        self.k = k

    def read(self, val):
        self.count += 1 # current element is the count-th element 
        r = random.randint(0, self.count - 1 ) # randomly generate a number from 0 to count(exclusive)[0,count-1]
        if r < self.k:
            self.sample[r] = val # the probability of choosing (count - 1)th element as the final solution is 1/count

    def get_sample(self):
        return self.sample


"""
Randomization
-------------
Design a random number generator Random(7), with Random(5)
Random(5)  -- 1/5 return 0,1,2,3,4
Random(7)  -- 1/7 return 0,1,2,3,4,5,6
"""
def random7():
    num = random25() # suppose there's already have this function
    while num > 6:
        num = random25()
        return num % 7 # similar to the 2D matrix for binary search


"""
Percentile
-----------
Given a certain number(100,000) of urls, how to find 95-th percentile of all url's length
"""
def percentile95(urls):
    """
    TC: O(n)
    SC: O(1)
    """
    buckets = [0 for i in range(4101)] # the length limit of url is 4100
    for url in urls:
        buckets[len(url)] += 1 # simulate a histgram 
    num = 0.95 * 100000
    total_so_far = 0
    for i in range(4101): # i is the url's length
        total_so_far += buckets[i]
        if total_so_far >= num:
            return i 



