#  Find Largest subarray sum 

# import sys

def KadaneAlgo(nums):
    max_sum = -1100000
    max_so_far = 0 

    for i in range(len(nums)):
        max_so_far += nums[i]
        if max_so_far > max_sum: 
            max_sum = max_so_far
        if max_so_far < 0:
            max_so_far = 0
    return max_sum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(KadaneAlgo(a))