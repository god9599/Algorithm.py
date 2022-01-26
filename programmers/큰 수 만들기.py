def solution(number, k):
    li = []
    cnt = 0
    for i in number:
        while li and i > li[-1]:
            if cnt < k:
                li.pop()
                cnt += 1
            else:
                break
        li.append(i)

    if cnt < k:
        for i in range(k):
            li.pop()

    return ''.join(li)
