# Deque >> double ended queue / 양방향 큐
# 표준모듈 >> from collections import deque
#제공함수 >> append, appendleft, pop, popleft, len

from collections import deque
deque = deque()

cnt3 = int(input("cnt >> "))
for _ in range(cnt3):
    functionName3, *num3 = input().split()
    # push_front
    if functionName3 == "push_front":
        deque.appendleft(int(num3[0]))
    # push_back
    if functionName3 == "push_back":
        deque.append(int(num3[0]))

    # pop_front
    elif functionName3 == "pop_front":
        if len(deque) != 0:
            print(deque.popleft())
        else:
            print(-1)
    # pop_back
    elif functionName3 == "pop_back":
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)

    # size
    elif functionName3 == "size":
        print(len(deque))

    # empty
    elif functionName3 == "empty":
        if len(deque) == 0:
            print(1)
        elif len(deque) != 0:
            print(0)

    # front
    elif functionName3 == "front":
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)

    # back
    elif functionName3 == "back":
        if len(deque) != 0:
            print(deque[len(deque)-1])
        else:
            print(-1)
