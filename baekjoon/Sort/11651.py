import sys

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(list(map(int, sys.stdin.readline().split())))
    numbers.reverse()

numbers.sort(key=lambda x:(x[1], x[0]))

for i in numbers:
    print("%d %d" %(i[0], i[1]))