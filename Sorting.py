## Q1: Bubble Sort

""" 
Idea: Swapping a,b, take a third variable t here, a->t, b->a, t-b
The outer loop for the iteration, and the inner loop is for pairs comparision.

Time Complexity: the sum of total input size-->O((n-1)+(n-2)+(n-3)+...+1) --> O(n^2) 
Space Complexity: O(1), the numbers swaped equal to the given array.
"""

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
Idea: Find the minumum(or maximum) in each search and bring it forward. 

Time Complexity: O(n^2)
Space Complexity: O(1)

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
Append first, then swap with the previous number if it's smaller.

Time Complexity: O(n^2)
Space Complexity: O(1) 
"""
def insert_num(array,number):
    array.append(number)
    # sort from the end to the front
    index=len(array)-1
    while index > 0: # O(n)
        if array[index-1] > array[index]:
            array[index-1], array[index]=array[index],array[index-1]
        else:
            break
        index -= 1
    print(array) # for debug

def insertion_sort(array):
    new_arr=[] # not Inplace anymore
    for i in range(len(array)): # O(n)
        insert_num(new_arr,array[i])
    return new_arr

array=[1,5,6,3,2]
new_array=insertion_sort(array)
print(array)
print(new_array)



## Q4: The Space Optimzed Insertion Sort: inplace instead of creation
"""
Like the inversed version of bubble sort.  
array=[1,2,3,5,4,9]
               k
               i

Time Complixity: O(n^2)
Space Complixity: O(1)
"""
def insertion_sort(array):
    for i in range(1, len(array)):
        k = i # index i is the newly added number
        while k > 0:  # O(n)
            if array[k-1] > array[k]:
                array[k-1], array[k]= array[k], array[k-1]
            else:
                break
            k -= 1

## Q6: The Time Optimized Insertion Sort 
"""
Time Complexity: O(n*logn)
"""

def insert_num(array,n):
    idx=len(array)
    """
    Utilizing the fact that the part before the insertion are already sorted.
    Using binary search to find the smallest number larger than n, 
    or the largest number smaller than n.
    """
    insert_index=binary_search(array,n) # O(logn)
    array.append(n) 
    while idx > insert_index:  # O(n)
        array[idx] = array[idx-1] 
        idx -= 1
    array[insert_index] = n

def insertion_sort(array):
    new_arr=[]
    for i in range(len(array)):
        insert_num(new_arr,array[i])
    return new_arr

## Q7: Advanced Sorting 

## Merge Sort
def merge_sort():
    """
    Split until get the single unit, merge the ordered subset into the new ordered set. 

    [38] [27] -> [27 38]
    [27,38][3,43] -> [3,27,38,43]

    new_list = [] 
        i
              j

    Time Complexity: O(n) -- Just iterate the two lists 
    Space Complexity: O(n) --when counting the output in it 
    """

def merge_sort_recursion():
    """
    check for the screenshot 
    Space Complexity: the expense are not happened at the same time, the old one will be retrieved. 
    and different from how time complexity is computed. 
    """

def quick_sort():
    """
    store_index is acting like a 隔板

    Space Complexity: O(1) -- all the operation are inplaced a
    """