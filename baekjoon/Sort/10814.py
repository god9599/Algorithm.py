import sys

N = int(sys.stdin.readline())
info_user = []

for _ in range(N):
    info_user.append(list(sys.stdin.readline().split()))

info_user.sort(key=lambda x: int(x[0]))

for i in info_user:
    print(i[0], i[1], end="\n")
