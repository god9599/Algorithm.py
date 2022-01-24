def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')

    while len(s) != 0:
        a = min(s, key=len)
        if len(answer) == 0:
            answer.append(int(a))
        else:
            b = a.split(',')
            for i in b:
                if int(i) not in answer:
                    answer.append(int(i))
        s.remove(a)

    return answer
