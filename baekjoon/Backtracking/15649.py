import sys

N, M = map(int, sys.stdin.readline().split())

check = [False] * N
answer = [0] * M

def permute(idx):
    if idx == M:
        for i in range(M):
            print(answer[i], end=' ')
        print()
        return
    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        answer[idx] = i+1
        permute(idx+1)
        check[i] = False

permute(0)

