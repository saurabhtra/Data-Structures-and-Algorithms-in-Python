n=4
board = ["."*n for _ in range(n)]
pdig =[0]*2*(n-1)
sdig=[0]*2*(n-1)
left = [0]*(n)
ans=[]
def solver(row,col):
    if col==n:
        ans.append(board[:])
    for row in range(n):
        if(left[row]==0 and pdig[row+col]==0 and sdig[n-1+(col-row)]==0):
            board[row] =board[row][:col]+"Q"+board[row][col+1:]
            left[row]=1
            pdig[row+col] =1
            sdig[n-1+(col-row)] =1
            solver(row,col+1)
            board[row] =board[row][:col]+ "."+board[row][col+1:]
            left[row]=0
            pdig[row+col] =0
            sdig[n-1+(col-row)] =0
solver(0,0)
print(ans)
            