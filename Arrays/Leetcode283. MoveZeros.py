# def moveZeroes(nums):
#     """
#     :type nums: List[int]
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
#     start =0 
#     n = len(nums)-1
#     idx = 0
#     if n < 1:
#         return
#     while start <=n and idx <=n:
#         while nums[idx] != 0 and idx < n:
#             idx+=1
#         while nums[start] == 0 and start < n:
#             start+=1
#         if start > idx  :
#             nums[start],nums[idx] =nums[idx],nums[start]
#             print("swap zeros",start,idx, nums[start],nums[idx])
#             idx +=1
#             start +=1
#         else:
#             if idx < n:
#                 start = idx+1
#             else:
#                 return
def moveZeroes(nums):
    start = 0
    n = len(nums)
    idx = 0
    while start < n:
        if nums[start] != 0:
            nums[idx] ,nums[start] = nums[start],nums[idx]
            idx +=1
        start+=1 
nums = [1,2,3]
moveZeroes(nums)
print(nums)