matrix =[[1,2,3,4]]
left = 0
right = len(matrix[0])
bottom = len(matrix)
top = 0
ans=[]
while top <= bottom and left <= right:
    for i in range(left,right):
        print("1nd loop is ruuning")
        ans.append(matrix[top][i])
    top+=1
    
    for i in range(top,bottom):
        print("2nd loop is ruuning")
        ans.append(matrix[i][right-1])
    right-=1
    if top < bottom:
        for i in range(-right+1,-left+1):
            print("3nd loop is ruuning")
            ans.append(matrix[bottom-1][abs(i)])
        bottom -=1
    if left < right:
        for i in range(-bottom+1,-top+1):
            ans.append(matrix[abs(i)][left])
        left+=1
print(ans)
    
