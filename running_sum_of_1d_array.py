nums = [1,2,3,4,5]

# def runningSum(nums):
#     n = len(nums)
#     for i in range(1, n):
#         nums[i] = nums[i] + nums[i-1]
#     return nums

def runningSum(nums):
    n = len(nums)
    lst = []
    a = 0

    for i in range(1, n):
        for j in nums:
            a = i + a
            lst[i] += nums[i-1]
            lst.append(nums)
    return lst

print(runningSum(nums))
