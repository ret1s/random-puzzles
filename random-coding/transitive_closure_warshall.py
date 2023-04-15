A = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]

n = len(A)
for j in range(n):
    for i in range(n):
        if A[i][j] == 1:
            for a in range(n):
                if A[j][a] == 1:
                    A[i][a] = 1
    
print(A)
                    
