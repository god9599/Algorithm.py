import sys

num = int(sys.stdin.readline())
count = 0

for i in range(num + 1):
    if i >= 1 and i <= 99:
        count += 1
    elif i >= 100:
        num_list = []
        for j in str(i):
            num_list.append(j)
        if (int(num_list[0]) + int(num_list[2])) / 2 == int(num_list[1]):
            count += 1

print(count)
