char_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
ans=[]
digits="45"
def solver(index,subset):
    if index>=len(digits):
        ans.append("".join(subset))
        return
    for ch in char_map[digits[index]]:
        subset.append(ch)
        solver(index+1,subset)
        subset.pop()
solver(0,[])
print(ans)