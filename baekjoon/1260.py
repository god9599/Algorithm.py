from collections import deque
import sys


n, m, start = map(int, sys.stdin.readline().strip().split())

edge = [[] for i in range(n + 1)]


for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for i in edge:
    i.sort()

dfs_check = [False for i in range(n + 1)]


def dfs(x):
    dfs_check[x] = True
    print(x, end=' ')
    for i in edge[x]:
        if dfs_check[i] == False:
            dfs(i)


def bfs():
    queue = deque([start])
    bfs_check = [False for i in range(n+1)]
    bfs_check[start] = True
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in edge[a]:
            if not bfs_check[i]:
                bfs_check[i] = True
                queue.append(i)


dfs(start)
print()
bfs()
