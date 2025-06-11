# https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated
# this ans (above link) is also good
nums=[-2,0,1,1,2]
nums.sort()
print(nums)
n = len(nums)

ans=[]
for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    j = i+1
    k = n-1
    while j <k:
        sum = nums[i]+nums[j]+nums[k]
        if sum > 0:
            k-=1
        elif sum < 0:
            j+=1
        else:
            ans.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
            while j <k and nums[j] == nums[j-1]:
                j+=1
            while j < k and nums[k] == nums[k+1]:
                k-=1
print(ans)