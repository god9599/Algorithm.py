import sys

dst = int(sys.stdin.readline())
cnt = 1

if dst == 1:
    cnt = 1
else:
    num = 1
    while dst > num:
        num += (cnt*6)
        cnt += 1

print(cnt)
