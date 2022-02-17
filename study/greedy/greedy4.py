def solution(people, limit):
    # 가벼운 무게부터 sorting
    people.sort()
    answer = 0

    # 앞에서부터는 가벼운 사람
    right = 0
    # 뒤에서부터는 무거운 사람
    heavy = len(people)-1

    # 가벼운 사람의 인덱스가 무거운 사람의 인덱스보다 작을때
    # (같을 때 -> 마지막 -> answer += 1 / 나머지 내용은 상관없음)
    while right <= heavy:
        # 구명보트 수 + 1
        answer += 1

        # 가벼운 사람 + 무거운 사람이 제한 무게보다 작거나 같다
        if people[right] + people[heavy] <= limit:
            # 가벼운 사람도 가고
            right += 1
            # 무거운 사람도 같이가고
        # 제한 무게보다 크면 무거운 사람부터 보낸다
        heavy -= 1

    return answer


print(solution([70, 50, 80, 50], 100))
