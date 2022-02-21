def solution(numbers):
    # str로 비교 (숫자 크기로 비교 X)
    numbers = list(map(str, numbers))

    # 첫번째 숫자로만 비교
    # numbers.sort(key=lambda x: x[0], reverse=True)
    # [3, 30, 34] -> [3, 30, 34]
    # [30, 34, 3] -> [30, 34, 3]
    # 그냥 들어온 순서대로 출력됨

    # 같은 숫자로 시작 : 3, 32, 320
    # ['320', '32', '3'] -> 원하는 모양 [3, 32, 320]
    # 320이 '자릿수가 많아서' 앞으로 배정된다

    # 자릿수를 맞춰준다 :
    # number : 0~1000_최소 3자리수로 만들어주면 비교가능
    # 320320320 vs 323232 vs 333

    # 1) 3 3 3
    # 2) 2 2 3 -> 333 (3)
    # 3) 0 3   -> 323232 (32)
    # 4) -> 320320320 (320)
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = "".join(numbers)

    # 테스트 케이스 11 [0,0,0,0] => 0000
    # 0으로 출력되어야
    answer = str(int(answer))
    return answer


print(solution([0, 0, 0, 0]))
