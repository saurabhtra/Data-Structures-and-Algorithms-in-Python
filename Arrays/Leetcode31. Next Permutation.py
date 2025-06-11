nums = [3,2,1]
j = len(nums)-1
while j > 0:
    if nums[j] > nums[j-1]:
        # nums[-1],nums[j-1] = nums[j-1],nums[-1]
        break
    j-=1
print(j)
# print(nums[j:])

if j==0:
    nums.sort()
    print(nums)
else:
    tobeswap =nums[j-1]
    print(nums[j-1])
    idx = len(nums)-1
    while idx >=j :
        if nums[idx] > tobeswap:
            print("swapwith = ", nums[idx])
            nums[j-1],nums[idx] =nums[idx],nums[j-1]
            
            break
        idx -=1
# nums = [2,5,4,3,2,1]
# print("new nums after swap = ", nums)
    nums[j:] = reversed(nums[j:])


# temp.sort()
# # print("temo =",temp)
# for n in temp:
#     nums[j] = n
#     j+=1
print(nums)
    
