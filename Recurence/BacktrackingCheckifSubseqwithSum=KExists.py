nums=[5,4,1,1,1,1,10]
target=9
# def solver(idx,total,subset):
#     if total == target:
        
#         return subset[:]
#     elif total > target:
#         return None
#     if idx>=len(nums):
#         return None
#     subset.append(nums[idx])
#     total+=nums[idx]
#     pick =solver(idx+1,total,subset)
#     if pick != None:
#         return pick
#     e=subset.pop()
#     not_pick =solver(idx+1,total-e,subset)
#     return  not_pick
# print(solver(0,0,[]))
def solver(idx,total):
    if total == target:   
        return True
    elif total > target:
        return None
    if idx>=len(nums):
        return None
    
    sum=total+nums[idx]
    pick =solver(idx+1,sum)
    if pick != None:
        return pick
    
    not_pick =solver(idx+1,total)
    return  not_pick
print(solver(0,0))