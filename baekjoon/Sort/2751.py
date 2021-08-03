import sys

input = sys.stdin.readline
num = int(input())
numList = []

for i in range(num):
    numList.append(int(input()))

numList.sort()

for i in numList:
    print(i)
