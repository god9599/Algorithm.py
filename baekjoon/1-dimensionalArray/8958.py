import sys

num = int(sys.stdin.readline())
list = []

for i in range(num):
    n = sys.stdin.readline()
    list = n
    sum = 0
    one = 1
    for j in list:
        if j == 'O':
            sum += one
            one += 1
        else:
            one = 1
    print(sum)
