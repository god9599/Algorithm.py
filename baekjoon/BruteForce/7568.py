import sys

N = int(sys.stdin.readline())
list_people = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    list_people.append([x,y])

for a in range(N):
    count = 1
    for b in range(N):
        if list_people[a][0] < list_people[b][0] and list_people[a][1] < list_people[b][1]:
            count += 1
    print(count, end = " ")