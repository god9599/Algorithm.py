import sys

N = int(sys.stdin.readline())
result = 0

for i in range(0, N):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if (s == N):
        result = i
        break

print(result)