A, B, C = map(int, input().split())

num_sales = 0

if B < C:
    num_sales = A // (C - B)
    print(num_sales + 1)

else:
    print(-1)