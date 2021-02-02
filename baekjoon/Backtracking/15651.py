n, m = map(int, input().split())
numbers = [i + 1 for i in range(n)]  # 1~n까지
is_number = [0 for _ in range(m)]  # 출력 개수

def dfs(idx):
    if idx >= m:
        print(*is_number)
        return
    for i in range(n):
        is_number[idx] = numbers[i]
        dfs(idx + 1)

dfs(0)