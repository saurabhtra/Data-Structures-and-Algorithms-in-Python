def findTarget(matrix,target):
    row = 0
    for i in range(len(matrix)-1):
        if target >= matrix[i][0] and target <= matrix[i+1][0]:
            if target == matrix[i][0] or target == matrix[i+1][0]:
                
                return True
            else:
                row = i
                break
        else:
            row = i+1
    #search in row
    for j in range(len(matrix[0])):
        if matrix[row][j] == target:
            return True
    return False
matrix =[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
print(findTarget(matrix,30))