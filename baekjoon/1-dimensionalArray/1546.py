import sys

num = int(sys.stdin.readline())

score_list = list(map(int, sys.stdin.readline().split()))
score = 0

M = max(score_list)

for i in range(num):
    score_list[i] = score_list[i] / M * 100
    score += score_list[i]

print(score / num)
