import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
number_of_sum = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if sum <= M:
                number_of_sum.append(sum)

print(max(number_of_sum))




