n=3
# nums=[0]*n
# ans=[]
# def solver(idx,flag,subset):
#     if idx >=len(nums):
#         ans.append(subset[:])
#         return
#     if flag:
#         temp =subset[:]
#         temp[idx]=0
#         solver(idx+1,True,subset)
#         temp[idx] = 1
#         solver(idx+1,False,temp)
#     else:
#         temp =subset[:]
#         temp[idx]=0
#         solver(idx+1,True,temp)
# solver(0,True,[0]*n)
# print(ans)


ans=[]
n=3
def solver(idx,flag,subset):
    if idx >= n:
        ans.append("".join(subset[:]))
        return
    if flag:
        solver(idx+1,True,subset)
        temp=subset[:]
        temp[idx]="1"
        solver(idx+1,False,temp)
    else:
        solver(idx+1,True,subset)
solver(0,True,["0"]*n)
print(ans)

