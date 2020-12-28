import sys

n = int(sys.stdin.readline())
nums = list(sys.stdin.readline())
result = 0

for i in range(n):
    result += int(nums[i])

print(result)
