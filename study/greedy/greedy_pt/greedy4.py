# 오름차순으로 합한다
# 누적의 합이 최소 -> 작은 수부터 더해야

n = int(input())

arr = list(map(int, input().split()))

# 오름차순 정렬
arr.sort()

result = 0
for i in range(n):
    for j in range(0, i+1):
        result += arr[j]

print(result)

# 5
# 3 1 4 3 2
# -> 3 + 4 + 8 + 11 + 13 = 39
# sort : 1 2 3 3 4
# -> 1 + 3 + 6 + 9 + 13 = 32


# 5
# 1 1 1 1 1
# -> 1 + 2 + 3 + 4 + 5 = 15
