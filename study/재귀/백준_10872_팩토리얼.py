#
# *팩토리얼 내용
# n = 0,1 -> n
# n != 1 -> n(n-1)! : 재귀

num = int(input())


def factorial(num):
    if num == 1 or num == 0:
        return 1

    return num * factorial(num-1)


print(factorial(num))
