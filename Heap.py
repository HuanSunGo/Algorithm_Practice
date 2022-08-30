
""" 
Logically, heap is a complete binary tree 
Heap Property: get the extreme values, max or min 
min-heap: pop the minimum of the collection, each node's value should <= the child node 
max-heap: each node's value >= the child node 


Array implementation: 
-------------------------
easy to store it as an array 
left_child_node_index: parent_node_index * 2 + 1
right_child_node_index: parent_node_index * 2 + 2 
parent_node_index: child_node_index - 1) //2 
"""

# Implement Heap with array 
from turtle import right


class Heap(object):
    def __init__(self):
        self.array = [] 

    def sift_up(array, index):
    
        """
               0 
             /    \
            1      5 
           /\      /\ 
           6  8   -1 
        arr = [0,1,5,6,8] -> push(-1) -> arr = [0,1,5,6,8,-1] -> change position -1 and 5, -1 and 0 -> [-1,1,0,6,8,5]

        Steps: sift-up operation 
        TC: O(h) --> O(logn)
        """
        parent_idx = (index - 1 ) // 2 
        if parent_idx < 0 or array[index] > array[parent_idx]:
            return 
        array[index],array[parent_idx] = array[parent_idx],array[index]
        sift_up(array, parent_idx) 

    def push(self,val):
        self.array.append(val)
        self.sift_up(self.array, len(self.array -1 ))
    
    # remove the root 
    """
    step 1: remove root 
    step 2: move the last leaf to root 
    step 3: sift-down for new root 
    """
    def sift_down_recursion(array, index):
        """
        TC: O(logn)
        SC: O(logn)
        """
        left_child = index * 2 + 1 
        right_child = index * 2 + 2 
        small = index 
        if left_child < len(array) and array[small] > array[left_child]:
            small = left_child
        if right_child < len(array) and array[small] > array[right_child]:
            small = right_child
            # after two ifs, small stores the smallest values' index
        if small != index:
            array[small], array[index] = array[index], array[small]
            sift_down_recursion(array, small)

    def sift_down_iteration(array, index):
        left_child = index * 2 + 1 
        right_child = index * 2 + 2 
        while left_child < len(array):
            if left_child < len(array) and array[small] > array[left_child]:
                small = left_child
            if right_child < len(array) and array[small] > array[right_child]:
                small = right_child
            if small == index:
                break 
            array[small], array[index] = array[index], array[small]
            index = small 
            left_child = index * 2 + 1 
            right_child = index *2 + 2 

    def pop(self):
        res = self.array[0]
        # the swap makes the TC only O(1)
        self.array[0],self.array[-1] = self.array[-1],self.array[0]
        # delete the end node and then sift 
        self.array.pop()
        self.sift_down_recursion(self.array, 0 )
        return res 

        # initialize a heap from a random array 
        """
        [5,4,3,2,1] -> min-heap 
        last element's index is len(arr)-1, the parent of last element is (len(arr)-1-1)//2
        """
    def build_heap(array):
        for i in range(len(array)//2-1, -1, -1):
            sift_down_recursion(array, i) 


# Python Heapq library : heapify(x)
## find smallest k elements from an unsorted array of size n 
### solution 0: sorting -> O(n)
### solution 1: min-heap 

import heapq 
def kSmallest(array, k):
    if not array: 
        return []
    res = []
    heapq.heapify(array)
    for i in range(min(k,len(array))):
        res.append(heapq.heappop(array))
    return res 
 








    