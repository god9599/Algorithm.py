def solution(N, stages):
    answer = []
    result = []
    dic = {k + 1: 0 for k in range(0, N)}
    for i in range(1, N + 1):
        cnt = 0
        people = 0
        if i == 1:
            people = len(stages)
        else:
            for k in stages:
                if k >= i:
                    people += 1
        if people == 0:
            answer.append(0)
            break
        for j in range(0, len(stages)):
            if i == stages[j]:
                cnt += 1
        answer.append(cnt / people)

    for i in range(0, len(answer)):
        dic[i + 1] = answer[i]

    li = sorted(dic.items(), key=lambda item: item[1], reverse=True)

    for i in li:
        result.append(i[0])

    return result
