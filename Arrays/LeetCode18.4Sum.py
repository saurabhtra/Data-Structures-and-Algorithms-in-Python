nums = [-2,-1,-1,1,1,2,2]
target = 0
n= len(nums)
nums.sort()
ans = []
for i in range(n):
    if i >0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1,n):
        if j > i+1 and nums[j] == nums[j-1]:
            continue
        p = j+1
        q = n-1
        while p<q:
            sums = nums[i]+nums[j]+nums[p]+nums[q]
            if sums < target:
                p+=1
            elif sums > target:
                q-=1
            else:
                ans.append([nums[i],nums[j],nums[p],nums[q]])
                p+=1
                q-=1
                while p <q and nums[p] == nums[p-1]:
                    p+=1
                while p <q  and nums[q] ==nums[q+1]:
                    q-=1
print(ans)
                
    