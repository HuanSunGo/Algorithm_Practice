## Q1: Bubble Sort

""" 
Idea: Swapping a,b, take a third variable t here, a->t, b->a, t-b
After the first iteration, we first got the biggest value at the end.

Time Complexity: 
"""

def bubble_sort(nums):
    # the outer loop: check the elements we have
    for i in range(len(nums)-1,0,-1): 
        # inner loop have decreasing numbers, because the last digit is determined from the previous loop as the biggest.
        for j in range(i):
            # start comparision from the begining
            if nums[j] > nums[j+1]: 
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[5,3,8,6,7,2]
bubble_sort(nums)
print(nums)
