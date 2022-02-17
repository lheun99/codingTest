n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    print(f"target: {target}")
    result += (n-target)
    print(f"result: {result}")
    n = target
    print(f"n: {n}")
    if(n < k):
        break

    result += 1
    print(f"result: {result}")

    n //= k
    print(f"n: {n}")

result += (n-1)
print(result)
