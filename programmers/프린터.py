from collections import deque


def solution(priorities, location):
    order = []
    li = deque([str(i) + str(priorities[i]) for i in range(len(priorities))])

    find = li[location]

    li.reverse()
    pri = deque(priorities)
    pri.reverse()

    while pri:
        if pri[-1] < max(pri):
            pri.appendleft(pri[-1])
            pri.pop()
            li.appendleft(li[-1])
            li.pop()
        else:
            order.append(li[-1])
            li.pop()
            pri.pop()

    return order.index(find) + 1
