# Stack >> FILO
# 사용연산_push, pop, top, empty, size
# stack은 모듈 없음 >> list로 구현 >> append, pop, len
cnt2 = int(input("cnt >> "))
stackList = list()

for _ in range(cnt2):
    functionName2, *num2 = input().split()
    # push
    if functionName2 == "push":
        stackList.append(int(num2[0]))
    # pop
    elif functionName2 == "pop":
        if len(stackList) != 0:
            print(stackList.pop())
        else:
            print(-1)
    # size
    elif functionName2 == "size":
        print(len(stackList))
    # empty
    elif functionName2 == "empty":
        if len(stackList) == 0:
            print(1)
        elif len(stackList) != 0:
            print(0)
    # front
    elif functionName2 == "top":
        if len(stackList) != 0:
            print(stackList[len(stackList)-1])
        else:
            print(-1)
