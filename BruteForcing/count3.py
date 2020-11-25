"""
입력:정수 N
출력: 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함된 모든 경우의 수
아이디어: 하루가 몇 초인지 생각해보자.
"""

N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)