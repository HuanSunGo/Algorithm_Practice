## Binary Search 

""" 
Ideas: For finding the position of the desired number, where the list should be sorted first. 
        Therefore don't need to check one half to improve the performance.

num:  sorted list i.e. nums=[1,2,4,5,7,8,9]
target: the number we're searching for i.e. target=4

Time Complexity: O(log(ns))
"""

def binary_search(nums, target): 
    if not nums: # corner case: if nums is None or len(nums)==0
        return None 
    l=0
    u=len(nums)-1
    while l <= u:
        mid = (l+u)//2 # get the integer division
        if nums[mid] > target:
            u=mid - 1
        elif nums[mid] < target:
            l=mid + 1 
        else:
            return mid 
    return None 



# Apply binary search in 2D space. 
"""
Matrix(n,m): first element of next row is larger than the last element of previous row. 
    [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

Time Complexity: log(mn)
Space Complexity: o (1), constant, since we didn't add anything

index= row_index*M + col_index
row_index= index // M
col_index= index % M

"""
def binary_search_2d(matrix, target):
    if not matrix:
        return None
    N,M=len(matrix),len(matrix[0]-1)
    l,u=0,N*M-1
    while l <= u:
        mid=(l+u)//2
        row_num= mid // 2
        col_num=mid % 2 
        if matrix[row_num][col_num] > target:
            u=mid-1
        elif matrix[row_num][col_num] < target:
            l=mid+1
        else:
            return(row_num, col_num)
    return None

# Find an element in the array that is clsest to the target number.
"""
The original binary search (while l <= u ) method will fall into dead loop.

i.e. nums=[1,2,5], target = 3
"""
def find_closest_num(nums, target): 
    if not nums: 
        return None 
    left=0
    right=len(nums)-1
    while left < right-1: # avoid the case when mid=left=right, since we didn't change -1 or +1
        mid = (left+right)//2 
        if nums[mid] > target:
            right=mid 
            """
            i.e [1,2,5,9] target=3, 
            """
        elif nums[mid] < target:
            left=mid 
        else:
            return mid 
    # compare the distance, need this because when existing the current while loop, there's still nums that haven't been compared
    return left if abs(nums[left]-target) < abs(nums[right]-target) else right

    # Find the index of the first occurrence of an element.