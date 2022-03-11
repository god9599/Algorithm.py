import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
start = 1
answer = 0
li = [[] for i in range(n+1)]

for i in range(m):
  s_node, e_node = map(int, sys.stdin.readline().strip().split())
  li[s_node].append(e_node)
  li[e_node].append(s_node)

dfs_check = [False for i in range(n+1)]

def dfs(x):
  dfs_check[x] = True
  for i in li[x]:
    if dfs_check[i] == False:
      dfs(i)


dfs(start)
print(dfs_check.count(True) - 1)