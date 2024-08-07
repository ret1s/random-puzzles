def q1(n, a, r):
    # Sn = [a(1-rn)] / (1-r) formula as google
    # return a * (1 - r**n) / (1 - r) => solution using formula
    total = 0
    for i in range(n):
        total += a * r**i
    return total

print(q1(4, 2, 3))


    