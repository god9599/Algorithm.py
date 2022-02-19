def solution(citations):
    answer = 0
    h = sum(citations) // len(citations)

    citations.sort()

    while True:
        up = 0
        for i in citations:
            if i >= h:
                up += 1
        if up >= h:
            answer = h
            break

        h -= 1

    return answer
