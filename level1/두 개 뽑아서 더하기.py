#from itertools import permutations as pm
from itertools import combinations as cb
# [(5, 0), (5, 2), (5, 7), (0, 5), (0, 2), (0, 7), (2, 5), (2, 0), (2, 7), (7, 5), (7, 0), (7, 2)]
# [(5, 0), (5, 2), (5, 7), (0, 2), (0, 7), (2, 7)]


def solution(numbers):
    #numbers1 = list(pm(numbers, 2))
    numbers = list(cb(numbers, 2))
    # print(numbers1)
    print(numbers)
    numList = []
    for one, two in numbers:
        numList.append(one + two)

    numList = list(set(numList))
    numList.sort()
    return numList


print(solution([5, 0, 2, 7]))
