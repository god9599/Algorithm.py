# 낮에 a만큼 올라가고, 밤에 b만큼 미끌어짐. v미터인 나무 막대 며칠 만에 올라가려나?
import sys
import math

a, b, v = map(int, sys.stdin.readline().split(' '))
day_one = a - b

day = (v-a) / day_one + 1
print(math.ceil(day))




