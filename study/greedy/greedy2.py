# 조이스틱

#name = list(map(name, input()))


def solution(name):
    answer = 0
    firstRightChangeMin = len(name)-1

    for i in range(len(name)):

        # UP DOWN
        # 알파벳 변경 A->B vs A->Z 이동 중 최소값 비교해서 넣어야 한다
        up = ord(name[i])-ord("A")
        down = (ord("Z")-ord(name[i])) + 1
        print(f"{name[i]} : up {up} down {down}")
        answer += min(up, down)

        # LEFT RIGHT
        # RIGHT : >로만

        # LEFT (right + left) : i까지 > 다음에는 <로 이동하는
        # 1) i+1에 "A"없으면
        # : i ->, i <-, 맨 뒤에서 i+1까지 (len(name)-back) <-
        # 2) "A"가 존재하면
        # : i ->, i <-, 맨 뒤에서 마지막 "A"뒤까지 (len(name)-back) <-
        back = i+1
        # "A"존재
        # 내부 순서도 중요 : 반대로 되면 range에러
        while(back < len(name) and name[back] == "A"):
            # "_AAA_" : 마지막 "A"의 인덱스
            back += 1

        left = i + i + (len(name) - back)

        # 각 i에서 이동 수 세서, 최소의 이동을 알아낸다
        # 처음의 min은 >로만 갔을 때 : right
        # 이 후에는 각 i 별로 비교 했을 때 최소의 인덱스
        print(
            f"{name[i]} : firstRightChangeMin {firstRightChangeMin} left {left}")
        firstRightChangeMin = min(firstRightChangeMin, left)
        print(f"    >> min {firstRightChangeMin}")

    answer += firstRightChangeMin
    return answer


print(solution("AABBAA"))
print(solution("JAN"))
