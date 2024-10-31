def func(x):
    return x* x * x - x * x + 2

def derivFunc(x):
    return 3 * x * x - 2 * x

def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    count = 1
    while abs(h) >= 0.0001:
        print("Iteration", count, ":", h)
        count += 1
        h = func(x) / derivFunc(x)
        x -= h
    return x

def main():
    # Newton's Method
    x0 = -20
    print("The value of the root using Newton's Method is : ", "%.4f"% newtonRaphson(x0))

if __name__ == "__main__":
    main()