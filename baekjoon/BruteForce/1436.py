import sys

N = int(sys.stdin.readline())
cnt = 0
end_sign = 666
while N:
    if '666' in str(end_sign):
       cnt += 1
    end_sign += 1
    if cnt == N:
        break

print(end_sign - 1)