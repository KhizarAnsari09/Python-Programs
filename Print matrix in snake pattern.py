def snake_matrix(matrix):
    
    count = 0
    b = []
    final = []
    for i in range(1,len(matrix),2):
        matrix[i] = matrix[i][::-1]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            final.append(matrix[i][j])
    
    print(*final)
    
if __name__ == '__main__':
    
    matrix = []
    n = int(input("Enter square matrix number: "))
    for i in range(n):
        a = []
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)
    snake_matrix(matrix)