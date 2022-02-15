def solution(lottos, win_nums):
    grade = []
    grade.append(6)

    for i in range(1, 7):
        grade.append(7 - i)

    zero_cnt = lottos.count(0)

    luck_cnt = 0
    for lotto_num in lottos:
        for win_num in win_nums:
            if lotto_num == win_num:
                luck_cnt += 1

    worst = luck_cnt
    best = zero_cnt + luck_cnt

    answer = []
    answer.append(grade[best])
    answer.append(grade[worst])

    return answer
