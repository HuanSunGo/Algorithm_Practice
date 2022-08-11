## Q1: Bubble Sort

""" 
Idea: Swapping a,b, take a third variable t here, a->t, b->a, t-b
The outer loop for the iteration, and the inner loop is for pairs comparision.

Time Complexity: the sum of total input size-->O((n-1)+(n-2)+(n-3)+...+1) --> O(n^2) 
Space Complexity: O(1), the numbers swaped equal to the given array.
"""

from turtle import left


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
def selection_sort_max(list):
    for i in range(len(list)-1, 0 ,-1):  # i = 6,5,4,3,2,1 
        max_index = 0 
        for j in range(i+1): # j = [0,7)
            if list[j] > list[max_index]:
                # update max number index 
                max_index = j
            # swap with the current last number: 
            list[j], list[max_index] = list[max_index], list[j]


def selection_sort_min(list):
    for i in range(len(list)):
        print('level:',i)  
        min_index=i
        for j in range(i,len(list)): 
            # find the min on each level 
            if list[j] < list[min_index]:
                print(list[j],'compare with',list[min_index])
                min_index=j
                print(f'min value is: {list[j]}')
        # jump out of j loop to swap
        list[i],list[min_index]=list[min_index],list[i]
        print('after swap',nums)

nums=[5,3,8,6,7,2]
selection_sort_min(nums)
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
    # starts from 1 because no need to compare for the first one
    for i in range(1, len(array)):
        k = i # index i is the newly added number
        print(f'level:{k}')
        while k > 0:  # O(n) -- need to restrain this because index could be negative and would go back 
            if array[k-1] > array[k]:
                array[k-1], array[k]= array[k], array[k-1]
            else:
                break
            print(array)
            # this k is within the while loop for comparing the current position with the left side part 
            k -= 1

array = [3,1,2,6,5,0]
insertion_sort(array)

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



## Merge Sort
def merge_sort(arr):
    """
    Split until get the single unit, merge the ordered subset into the new ordered set. 
    Compare the left most element of an array, and the left most of the other. 

    [38] [27] -> [27 38]
    [27,38][3,43] -> [3,27,38,43]

    new_list = [] 
        i
              j

    Time Complexity: O(n*logn)  --each level's time complexity * level 
    Space Complexity: O(n) --recursion level (logn) + newly build array number(n) = O(n)
    
    """
    if len(arr) > 1: 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursiono 
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge step 
        i = 0 # left_arr index 
        j = 0 # right_arr index 
        k = 0 # merge array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else: 
                arr[k] = right_arr[j]
                j += 1 
                k += 1
        
        # when there's still element missing from the left/right array to transfer to the merge array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(left_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [2,3,5,1,7,4,4,2,6,0]


def quick_sort(arr):
    """
    Find the pivot point and put the smaller one and bigger one into two arrays, do it recursively.
    Here we use the last one as the pivot. 

    Time Complexity: average -- O(n*logn), worst case -- O(n^2)
    Space Complexity: average --O(n*logn), worst case -- O(n)
    """
    if len(arr) <= 1:
        return arr
    else: 
        pivot = arr.pop() # remove the last element of the sequence and return it 

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot: 
            items_greater.append(item)
        else: 
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# test case
print(quick_sort([2,3,5,1,7,4,4,2,6,0]))