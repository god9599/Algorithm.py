"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행. 두 번째 연산은 N이 K로 나누어
떨어질 때만 선택 가능
1. N에서 1을 뺸다.
2. N을 K로 나눈다.
입력 : N, K
출력 : N이 1이 될 때까지 수행해야 하는 연산 횟수의 최솟값
"""

n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)