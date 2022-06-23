arr = [x for x in range(1, 11)]


def func(x):
    return x * x


print(list(map(func, arr)))
print([func(x) for x in arr if not x % 2])


def is_even(x):
    return x % 2 == 0


print(list(map(func, filter(is_even, arr))))
