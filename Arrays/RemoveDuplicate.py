#nums= [1,1,2,3,3,3,4,4]
def removeDuplicate(nums):
    curr = 1
    prev = 0
    n = len(nums)
    while curr < n:

        if nums[prev] == nums[curr]:
            flag = True
            pass
        else:
            nums[prev+1] = nums[curr]
            prev+=1
            
        

        curr+=1
nums= [1,2,3,3,3,4,4,5,6]
removeDuplicate(nums)
print(nums)