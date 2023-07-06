"""
Given an array of integers nums and an integer k, 
return the all subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example: [1, -1, 0] k=0
Output = [
    [1,-1]
    [1,-1,0]
    [0]
]

"""

def find_sub_arrays_target_sum(nums , k):
    N = len(nums)
    prefix = [nums[0]]
    for i in range(1, N):
        prefix.append(nums[i] + prefix[-1])

    results = []
    for i in range(N):
        for j in range (i, N):
            currSum = prefix[j] - prefix[i] + nums[i]
            if currSum == k:
                results.append(nums[i:j+1])
    
    return results

test_cases = [
    [[1,2,0,4,-1,-3,-2], -5]
]
for nums, k in test_cases:
    print('====')
    print(nums, k)
    print('====')
    for arr in find_sub_arrays_target_sum(nums, k):
        print(arr, sum(arr))