# nums=[5,9,4,6,3]
# target=9
# ans=[]
# def solver(idx,total,subset):
#     if total==target:
#         ans.append(subset.copy())
#         return
#     elif total >target:
#         return
#     if idx >=len(nums):
#         return
    
    
#     subset.append(nums[idx])
#     total=total+nums[idx]
#     solver(idx+1,total,subset)
#     e=subset.pop()
#     total -=e
#     solver(idx+1,total,subset)
# solver(0,0,[])
# print(ans)
candidates = [10,1,2,7,6,1,5]
target = 8
ans=[]
dup =set()
def solver(idx,total,subset):
    if total ==target:
        print(total, subset)
        subset.sort()
        
        dup.add(tuple(subset[:]))
            # ans.append(subset[:])
        return
    elif total >target:
        return
    if idx>=len(candidates):
        return
    subset.append(candidates[idx])
    total +=candidates[idx]
    solver(idx+1,total,subset)
    e=subset.pop()
    total -=e
    solver(idx+1,total,subset)
solver(0,0,[])
print(dup)