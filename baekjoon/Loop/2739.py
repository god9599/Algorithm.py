import sys

N = int(sys.stdin.readline())

def gugudan(n):
    for _ in range(1, 10):
        print('%d * %d = %d' %(n, _, n*_))

gugudan(N)
