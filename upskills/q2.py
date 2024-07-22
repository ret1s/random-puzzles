def q2(requested_amount, availabe=[]):
    total = 0
    res = {}
    while total < requested_amount:
        current = max(available)
        res[current] = math.floor(requested_amount/current)
        total += current*res[current]
        requested_amount -= total
        available.remove(current)
        if len(availabe) == 0 and total < requested_amount:
            raise ValueError("Requested amount cannot be multipled with available values")
    
    for a, b in res:
        print(f'{b} money notes of {a}')
    
    

        