num = set(range(1, 10001))
self_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    self_num.add(i)

num = num - self_num

for k in sorted(num):
    print(k)
