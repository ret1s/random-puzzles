def q3(N, M):
    # if M < N:
    #     raise ValueError("Invalid input")

    fib_list = []
    a, b = 0, 1
    index = 0
    
    while index <= M:
        if index >= N:
            fib_list.append(a)
        index += 1
        a, b = b, a + b
    
    return sum(fib_list)

print(q3(3, 6))