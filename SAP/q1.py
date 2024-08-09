A = [1, 3, 15, 11, 2] # n: size A
B = [23, 127, 235, 19, 8] # m: size B

min = 1000000
a = -1
b = -1
# for i in A:
#     for j in B:
#         val = i - j
#         if val < 0:
#             val = -val
#         if val < min:
#             min = val
#             a = i
#             b = j
C = A + B
for i in range(len(C) - 1):
    val = C[i] - C[i + 1]
    if val < 0: 
        val = -val
    if val < min:
        min = val
        a = C[i]
        b = C[i + 1]

print(min)
print(a)
print(b)