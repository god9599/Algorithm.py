remain = []

for i in range(10):
    num = int(input())
    if num % 42 not in remain:
        remain.append(num % 42)

print(len(remain))