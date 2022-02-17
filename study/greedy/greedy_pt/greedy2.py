# 대부분 + 보다는 * 가 큰 값을 만든다
# 예외적으로 두 수 중 하나라도 0, 1이면 +가 더 큰 값을 만든다
# -> 20*0 = 0 vs. 20+0 = 20


nums = input()

result = int(nums[0])
for i in range(1, len(nums)):
    num = int(nums[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
