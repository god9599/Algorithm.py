"""
입력 조건
- 두 정수 n, m(4<=n, m<=200)이 주어진다.
- n개의 줄에는 각각 m개의 정수(0또는 1)로 미로의 정보가 주어진다. 시작 칸과 마지막 칸은 항상 1
출력 조건
- 첫째 줄에 최소 이동 칸의 개수를 출력
"""

from _collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))