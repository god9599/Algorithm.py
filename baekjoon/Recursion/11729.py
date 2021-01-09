import sys

def move_hanoi(board, start, end, other):
    if board == 1:
        print(start, end)

    else:
        move_hanoi(board-1, start, other, end)
        print(start, end)
        move_hanoi(board-1, other, end, start)


N = int(sys.stdin.readline())

print(2**N-1)
move_hanoi(N, 1, 3, 2)

