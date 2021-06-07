import sys

num = int(sys.stdin.readline())
arr1 = list(map(int, input().split()))

arr2 = sorted(list(set(arr1)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr1:
    print(dic[i], end=' ')
