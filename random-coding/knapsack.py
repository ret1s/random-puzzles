M = 17
N = 5
size = [3, 4, 7, 8, 9]
val = [4, 5, 10, 11, 13]
items = {
    0: "-",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E"
}
cost = [0] * M
best = [0] * M
for j in range(N): # number of items
    for i in range(M): # capacity
        capacity = i + 1
        if capacity >= size[j]:
            last_size = max(i - size[j], 0)
            if cost[i] < cost[last_size] + val[j]:
                cost[i] = cost[last_size] + val[j]
                best[i] = j + 1
    print(f"Cost: {cost}")
    print("Best:", end = " ")
    for i in range(M):
        print(items[best[i]], end=" ")
    print()


