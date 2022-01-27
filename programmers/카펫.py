def solution(brown, yellow):
    li = []  # yellow의 약수들의 경우의 수

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if yellow // i < i:  # 가로가 더 짧은 경우
                continue
            else:  # 가로가 더 긴 경우
                li.append((yellow // i, i))

    for i in li:
        a = (2 * i[0]) + (2 * i[1]) + 4
        if a == brown:
            return [i[0] + 2, i[1] + 2]
