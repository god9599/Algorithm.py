import sys

num = int(sys.stdin.readline())
stage = 1

while True:
    if num > stage:
        num -= stage
        stage += 1
    else:
        break

if stage % 2 == 0:
    print('%d/%d' %(num, stage-(num-1)))
else:
    print('%d/%d' %(stage-(num-1), num) )


