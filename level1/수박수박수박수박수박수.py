def solution(n):
    subak = "수박"
    cnt = n % 2
    if cnt == 0:
        cnt = n//2
        return subak*cnt
    elif cnt != 0:
        cnt = n//2
        return (subak*cnt)+"수"


print(solution(1001))
print(solution(4))
