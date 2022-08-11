# Reference: https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

## Q1: Binary Search 

""" 
Ideas: For finding the position of the desired number, where the list should be sorted first. 
        Therefore don't need to check one half to improve the performance.

num:  sorted list i.e. nums=[1,2,4,5,7,8,9]
target: the number we're searching for i.e. target=4

Time Complexity: O(log(n))
"""

def binary_search(nums, target): 
    if not nums: # corner case: if nums is None or len(nums)==0
        return None 
    l=0
    u=len(nums)-1
    while l <= u: # can result in the dead loop sometimes 
        mid = (l+u)//2 # get the integer division
        if nums[mid] > target:
            u=mid - 1
        elif nums[mid] < target:
            l=mid + 1 
        else:
            return mid 
    return None 

binary_search([1,3,8,9,12,25],12)

# LeetCode74: Apply binary search in 2D space. 
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
    N,M=len(matrix),len(matrix[0])
    l,u=0,N*M-1
    while l <= u:
        mid=(l+u)//2
        row_num= mid // M
        col_num=mid % M
        if matrix[row_num][col_num] > target:
            u=mid-1
        elif matrix[row_num][col_num] < target:
            l=mid+1
        else:
            return(row_num, col_num)
    return None

# Q3: Find an element in the array that is clsest to the target number.
"""
The original binary search (while l <= u ) method will fall into dead loop when l=r= happens 

i.e. nums=[1,2,5], target = 3
"""
def find_closest_num(nums, target): 
    if not nums: 
        return None 
    left=0
    right=len(nums)-1
    while left < right-1: # more recommended way: avoid the case when mid=left=right, since we didn't change -1 or +1
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

# Q4: Find the index of the last occurrence of an element.

def find_last_occurrence(nums,target):
    if not nums:
        return None
    left = 0
    right=len(nums)-1
    while left < right -1: # more generalized condition, so that middle won't be the same as left or right pointer 
        mid=(left+right)//2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else: 
            """when nums[mid]==target, still possible to have the last occurrence on the right part"""
            left = mid 
        # Postprocessing here: when the while condition won't satisfied, and the left pointer meet with the right pointer  
        if nums[right] == target:
            return right
            # cannot change the sequency of this two if conditions
        if nums[left] == target:
            return left
        return None


# LeetCode34: Find the first and the last position of the sorted array.
"""
Input: nums = [5,7,7,8,8,8,10], target = 8
Output: [3,5]
"""

class Solution:
    
    def searchRange(self, nums: list[int], target: int) -> List[int]:
        lower_bound=self.findBound(nums,target,True)
        if(lower_bound == -1):
            return [-1,-1]
        upper_bound=self.findBound(nums,target,False)
        return [lower_bound,upper_bound]
        
    def findBound(self, nums:list[int], target:int, isFirst:bool) -> int:
        begin, end =0, len(nums)-1
        while begin <= end: 
            mid=(begin+end)//2
            if nums[mid] > target: 
                end=mid - 1
            elif nums[mid] < target: 
                begin=mid + 1
            # now for the case when nums[mid]==target, two scenarios
            else: 
                if isFirst:
                    # now try to find the lower bound
                    if mid == begin or nums[mid - 1] < target: 
                        return mid 
                    # not ideal, continue search on the left side for lower bound 
                    end = mid - 1 
                else:
                    # find the upper bound
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1
        return -1


class Solution_2:

    def search_range(self, nums, target):
        """
        Main function
        : type nums: list[int]
        : type target: int
        : rtype: list[int]
        """
        result = [-1, -1]
        result[0] = self.search_left(nums,target)
        result[1] = self.search_right(nums,target)

        return result 

    # helper function 1: find the first occurance
    def search_left(self, nums, target):
        index = -1
        begin, end = 0, len(nums)-1

        while begin <= end : 
            mid = (begin + end ) // 2 
            if nums[mid] == target:
                index = mid 
                end = mid - 1 
            elif nums[mid] > target: 
                end = mid - 1 
            else:
                begin = mid + 1 

        return index 
    
    # helper function 2: find the last occurance
    def search_right(self, nums, target): 
        index = -1 
        begin, end= 0, len(nums)-1

        while begin <= end:
            mid = (begin+end)//2
            if nums[mid] == target:
                index = mid 
                begin = mid + 1 
            elif nums[mid] > target:
                end = mid - 1 
            else:
                begin = mid + 1 
        return index 

nums= [5,7,7,8,8,8,10]
target = 8
ans=Solution_2()
ans.search_range(nums,target)
        
## Q5: Find the largest integer whose square is less than or equal to the given integer.
def square_root(n):
    """
    Parameters:
    ---------------------------
    input: non-negative integer 
    output: non-negative integer

    Logic:
    ----------------------------
    Solution1: try every number in [1,n]
        val = 1
        while val * val <= n:
            val += 1 
        return val - 1 
    # Time Complexity: O(n), Space Complexity: O(1)

    Solution2 : sorted array -> binary search 
        if mid * mid < n: go right 
        if mid * mid > n: go left 
        if mid * mid == n: return mid 
    # Time Complexity: O(logn), Space Complexity: O(1)
    """
    if n <= 1: 
        return n 
    left, right = 1, n//2 # since n^2 grows much quicker than n//2
    
    while left < right - 1: # to avoid the overlaping
        mid = (left + right) // 2 
        midsq = mid * mid 
        if midsq == n:
            return mid 
        elif midsq > n:
            right = mid 
        else: 
            left = mid 
    if right * right <= n:
        return right 
    else:
        return left 

# test code 
print(square_root(300))
