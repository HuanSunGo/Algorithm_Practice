## Q1: Bubble Sort

""" 
Idea: Swapping a,b, take a third variable t here, a->t, b->a, t-b
The outer loop for the iteration, and the inner loop is for pairs comparision.

Time Complexity: the sum of total input size-->O((n-1)+(n-2)+(n-3)+...+1) --> O(n^2) ONLY take the highest level of 
"""

from re import L


def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1): 
        print('level:',i) # for debug
        for j in range(i): # [0,i)
            print('compare:',j) # for debug 
            if nums[j] > nums[j+1]: 
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                print('after swap:',nums) # for debug
                """
                Python easier syntax:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                """

nums=[5,3,8,6,7,2]
bubble_sort(nums) # inplace
print(nums)

## Q2: Selection Sort

""" 
Idea: Unlike the multiple iteration in bubble sort, find the minumum(or maximum) in each search and bring it forward.

Time Complexity: O(n^2)
Space Complexity: O(1)

O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)

"""

def selection_sort(nums):
    for i in range(len(nums)):
        print('level:',i)
        min_index=i
        for j in range(i,len(nums)): # unlike the bubble sorting, need to go to the end to invistigate
            if nums[j] < nums[min_index]:
                print(nums[j],'compare with',nums[min_index])
                min_index=j
        # jump out of j loop to swap
        nums[i],nums[min_index]=nums[min_index],nums[i]
        # print('after swap',nums)

nums=[5,3,8,6,7,2]
selection_sort(nums)
print(nums)

## Q3:Insertion Sort
"""
Add new elements in the already ordered sequence. 
Append first, then swap with the precending number if it's smaller.

Time Complexity: two iterations interaction with each other, n * n
Space Complexity: create new list 
"""
def insert_num(array,number):
    array.append(number)
    index=len(array-1)
    while


## Q4: The Optimized Insertion Sort: inplace instead of creation
"""
i being the newly added number. Like the inversed version of bubble sort.  
array=[3,1,2,6,5,0]
         k
           i
Time Complixity: O(n^2)
Space Complixity: O(1)

"""
def insertion_sort(array):
    for i in range(1, len(array)):
        k = i # index i is the newly added number
        while k > 0:  # O(n)

