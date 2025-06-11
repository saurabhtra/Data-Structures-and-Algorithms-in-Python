ans=[]
target=7
candidates=[2,3,6,7]
def solver(idx,total,subset):
    
    if  total==target:
        
        ans.append(subset[:])
        return
    if total>target:
        return
    if idx>=len(candidates):
        return
    subset.append(candidates[idx])
    sums=total +candidates[idx]
    print(subset,sums,total)
    solver(idx,sums,subset)
    if len(subset)!=0:
        e=subset.pop()
    else:
        e=0
    
    solver(idx+1,total,subset)
solver(0,0,[])
print(ans)