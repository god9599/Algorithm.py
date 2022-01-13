def solution(dartResult):
    answer = 0
    li = []

    for i in dartResult:
        if i.isdigit() == True:
            if len(li) != 0 and str(li[-1]) + i == '10':
                li[-1] = 10
            else:
                li.append(int(i))
            continue
        if i == 'S':
            li[-1] = int(li[-1])**1
        elif i == 'D':
            li[-1] = int(li[-1])**2
        elif i == 'T':
            li[-1] = int(li[-1])**3
        elif i == '*':
            if len(li) == 1:
                li[-1] = li[-1] * 2
            elif len(li) >= 2:
                li[-1] = li[-1] * 2
                li[-2] = li[-2] * 2
        elif i == '#':
            if len(li) == 1:
                li[-1] = li[-1] * -1
            elif len(li) >= 2:
                li[-1] = li[-1] * -1

    for j in li:
        answer += int(j)

    return answer
