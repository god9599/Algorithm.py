def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()

    for _lost in lost[:]:
        if _lost in reserve:
            answer = answer + 1
            lost.remove(_lost)
            reserve.remove(_lost)
            print(lost[:])

    for _lost in lost[:]:
        if (_lost - 1) in reserve:
            answer = answer + 1
            reserve.remove(_lost - 1)
            continue
        elif (_lost + 1) in reserve:
            answer = answer + 1
            reserve.remove(_lost + 1)
    return answer
