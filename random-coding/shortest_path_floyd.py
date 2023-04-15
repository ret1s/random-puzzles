A = [
    [0, -1, 3, -1],
    [2, 0, -1, -1],
    [-1, 7, 0, 1],
    [6, -1, -1, 0]
]

n = len(A)
P = [[0] * n for i in range(n)] 

print(f"A0: {A}")
print(f"P0: {P}")

for j in range(n):
    for i in range(n):
        if A[i][j] > 0:
            for a in range(n):
                if A[j][a] > 0:
                    if A[i][a] == -1:
                        P[i][a] = j + 1
                        A[i][a] = A[i][j] + A[j][a] 
                    elif A[i][j] + A[j][a] < A[i][a]:
                        P[i][a] = j + 1
                        A[i][a] = A[i][j] + A[j][a] 
    print(f"A{j + 1}: {A}")
    print(f"P{j + 1}: {P}")
    
    