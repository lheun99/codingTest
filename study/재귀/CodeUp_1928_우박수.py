#
# *우박수
# n -> 홀수 : 3n+1
#      짝수 : n/2
# n이 1이 될 때까지, 반복

num = int(input())


def collatz(num):
    print(int(num))

    if num == 1:
        return
    elif num % 2 != 0:
        collatz((3*num)+1)
    elif num % 2 == 0:
        collatz(num/2)


collatz(num)
