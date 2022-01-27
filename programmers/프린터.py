from collections import deque


def solution(priorities, location):
    queue = deque([(i, j) for i, j in enumerate(priorities)])
    find = queue[location]
    queue.reverse()
    order = []

    while queue:
        a = _max(queue)
        if queue[-1][1] < a:
            queue.appendleft(queue[-1])
            queue.pop()
        else:
            order.append(queue[-1])
            queue.pop()

    return order.index(find) + 1


def _max(li):
    maxx = 0
    for i in li:
        if i[1] > maxx:
            maxx = i[1]
    return maxx
