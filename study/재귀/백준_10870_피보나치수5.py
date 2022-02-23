#
# *피보나치수 Fibonacci
# fn = fn-1 + fn-1

num = int(input())


def fibonacci(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(num))
