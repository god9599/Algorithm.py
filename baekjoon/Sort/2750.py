import sys

N = int(sys.stdin.readline())
num_list = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)
num_list.sort()
for _ in range(N):
    print(num_list[_])