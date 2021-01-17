import sys

n = int(sys.stdin.readline())
numbers = list(str(n))

numbers.sort()
numbers.reverse()

for _ in numbers:
    print(_, end = "")



