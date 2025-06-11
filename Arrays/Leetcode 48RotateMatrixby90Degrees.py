matrix = [[1,2,3],[4,5,6],[7,8,9]]
def Transpose(matrix):
    r= len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if j > i:
                matrix[i][j],matrix[j][i] = matrix[j][i] ,matrix[i][j]
    print(matrix)
Transpose(matrix)
def reverseRows(matrix):
    r= len(matrix)
    for i in range(r):
        matrix[i].reverse()
    print(matrix)
reverseRows(matrix)