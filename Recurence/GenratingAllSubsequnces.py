nums=[1,2,3]
ans=[]
def solver(idx,subset):
    if idx>=len(nums):
        ans.append(subset.copy())
        return 
    subset.append(nums[idx])
    solver(idx+1,subset)
    subset.pop()
    solver(idx+1,subset)
solver(0,[])
print(ans)