import sys

a = sys.stdin.readline().strip()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    a = a.replace(i, 'a')

print(len(a))
