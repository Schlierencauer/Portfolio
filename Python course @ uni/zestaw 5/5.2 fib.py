

def pamiec(func):
    slownik = {}
    def wrapper(x):

        if x in slownik:
            return slownik[x]
        else:
            wartosc = func(x)
            slownik[x] = wartosc
            return wartosc
    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(100):
    print(fibonacci(i))