def solution(s):
    answer = 0
    li = []

    for i in s:
        if len(li) == 0:
            li.append(i)
        else:
            if i == li[-1]:
                del li[-1]
            else:
                li.append(i)

    if len(li) == 0:
        answer = 1

    return answer
