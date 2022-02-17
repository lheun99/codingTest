def solution(name):
    answer = 0
    n = len(name)

    # 동일 내용 출력
    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    # move : >만 했을 때,
    move = n - 1

    # name의 idx
    for idx in range(n):
        # 해당 idx+1
        next_idx = idx + 1
        # range에러 막기 + 다음이 A인거에 대한 체크 내용도 동일
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1

        # distance :
        print(f"idx : {idx}, n - next_idx : {n}-{next_idx} = {n - next_idx}")
        distance = min(idx, n - next_idx)
        print(f"distance {distance}")
        # move :
        print(f"move : {move}")
        print(
            f"idx + n - next_idx + distance : {idx} + {n} - {next_idx} + {distance} : {idx + n - next_idx + distance}")
        move = min(move, idx + n - next_idx + distance)
        print(f"move: {move}")
    answer += move
    return answer


print(solution("JANAN"))
