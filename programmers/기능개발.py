from collections import deque


def solution(progresses, speeds):
    answer = []
    day = []  # 각 작업마다 남은 일 수
    for i, j in zip(progresses, speeds):
        a = 100 - i
        if a % j > 0:
            day.append((a // j) + 1)
        else:
            day.append(a // j)

    li = deque()

    for i in day:
        if len(li) == 0:
            li.append(i)
        else:
            if li[0] >= i:
                li.append(i)
            else:
                answer.append(len(li))
                li.clear()
                li.append(i)

    answer.append(len(li))
    return answer
