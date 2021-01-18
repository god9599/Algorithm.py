import sys

N = int(sys.stdin.readline())
strings = []
sort_list = []

for _ in range(N):
    strings.append(sys.stdin.readline().rstrip())

remove_duplicate_strings = list(set(strings))# 중복제거

for i in remove_duplicate_strings:
    sort_list.append((i, len(i)))

sort_list.sort(key=lambda x:(x[1], x[0]))# 길이순으로 정렬한 뒤에 사전 순으로 정렬

for i in sort_list:
    print(i[0], end="\n")