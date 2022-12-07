# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:

# *********************************************************

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# *********************************************************

# SOLUTION BIG O(n)

def pivotIndex(nums):
    total = sum(nums) 
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return f"The pivot index is {i}" 
        leftSum += nums[i]
    return -1

nums = [1,7,3,6,5,6]

print(pivotIndex(nums))

# About the approach 
# Take the toatal value (sum) of the array. 
# Sutract it from the leftSum and also from the pivot value { nums[i]} we currently at.
# Returning the index of pivot, not the value at that index
