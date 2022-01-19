def solution(scoville, K):
    answer = 0
    a = 0
    b = 0

    while min(scoville) < K:
        a = min(scoville)
        scoville.remove(a)
        b = min(scoville)
        scoville.remove(b)

        scoville.append(a + (b * 2))
        answer += 1

        if len(scoville) == 1:
            if scoville[0] < K:
                return -1

    return answer
