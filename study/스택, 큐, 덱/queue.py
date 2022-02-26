# Queue >> FIFO
# 사용연산_push, pop, front, empty

# import queue >> 표준모듈
# 제공함수 >> put, get, qsize, empty

import queue
que = queue.Queue()

cnt = int(input("cnt >> "))
for _ in range(cnt):
    functionName, *num = input().split()
    # push
    if functionName == "push":
        que.put(int(num[0]))
    # pop
    elif functionName == "pop":
        if que.empty() == False:
            print(que.get())
        else:
            print(-1)
    # size
    elif functionName == "size":
        print(que.qsize())
    # empty
    elif functionName == "empty":
        if que.empty() == True:
            print(1)
        elif que.empty() == False:
            print(0)
    # front
    elif functionName == "front":
        if que.empty() == False:
            print(que.queue[0])
        else:
            print(-1)
    # back
    elif functionName == "back":
        if que.empty() == False:
            print(que.queue[que.qsize()-1])
        else:
            print(-1)
