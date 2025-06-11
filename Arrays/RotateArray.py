#nums = [1,2,3,4,5,6,7] ->[7,1,2,3,4,5,6]
def RightRotate(nums):
    temp = nums[-1]
    n = len(nums)-1
    while n > 0:
        nums[n] = nums[n-1]
        n-=1
    nums[n] = temp
    print(nums)

nums = [1,2,3,4,5,6,7]
RightRotate(nums)