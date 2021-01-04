n, k = map(int, input().split(' '))

n_1 = int(str(n)[::-1])
k_1 = int(str(k)[::-1])

if (n_1 > k_1):
    print(n_1)
elif (n_1 < k_1):
    print(k_1)
