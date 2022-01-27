from itertools import combinations


def solution(clothes):
    answer = 0
    dic = {i[0]: i[1] for i in clothes}
    li = []  # 옷 종류 담는 곳

    for i in dic.values():
        li.append(i)
    li = list(set(li))

    cnt = []  # 옷 종류마다 옷의 개수 담는 곳
    for i in li:
        c = 0
        for j in dic.values():
            if i == j:
                c += 1
        cnt.append(c)

    a = 1
    for i in cnt:
        a *= (i+1)

    return a - 1
