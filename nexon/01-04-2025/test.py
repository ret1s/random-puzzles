# cook your dish here
def foo(value):
    while True:
        value = (yield value)
bar = foo(1)
print(next(bar))
print(next(bar))
print(bar.send(2))
