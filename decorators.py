import math
import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__} is {end - start}")
        return ret

    return inner


@calculate_time
def my_factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


@calculate_time
def math_factorial(num):
    return math.factorial(num)


if __name__ == "__main__":
    print(my_factorial(20))
    print(math_factorial(20))
