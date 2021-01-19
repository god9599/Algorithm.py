import sys

N, M = map(int, sys.stdin.readline().split())

use_check = [True] * N
numbers = []
List = []
for i in range(N):
    List.append(i + 1)

def compute(idx):
    global use_check, numbers
    if idx == M:
        print(*numbers)
        return

    for i in range(idx, N):
        if not use_check[i]:
            continue
        use_check[i] = False
        numbers.append(List[i])
        compute(idx + 1)
        numbers.pop()
        for j in range(i + 1, N):
            use_check[j] = True

compute(0)