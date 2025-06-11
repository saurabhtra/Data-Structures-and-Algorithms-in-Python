#nums = [1,2,3,4,8,7]
def findSecondLargest(nums):
    largest = nums[0]
    secLargest = nums[0]
    for n in nums:
        largest = max(n,largest)
        if n < largest and n >secLargest:
            secLargest = n
    return secLargest
    
nums = [7,7]
print(findSecondLargest(nums))
