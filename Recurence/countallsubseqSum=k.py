nums=[5,4,1,1,1,1,9,10]
target=9
def solver(idx,total,count):
    if total==target:
        count+=1
        return count
    elif total>target:
        return 0
    if idx>=len(nums):
        return 0
    sum=total+nums[idx]
    return solver(idx+1,sum,count)+solver(idx+1,total,count)
    
print(solver(0,0,0))
