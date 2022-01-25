def solution(s):
    answer = []
    num = (len(s) // 2) + 1

    if len(s) == 1:
        return 1

    for i in range(1, num):
        cnt = 1
        result = ''
        temp_s = s[:i]

        for j in range(i, len(s), i):
            if temp_s == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    result += str(cnt) + temp_s
                else:
                    result += temp_s
                temp_s = s[j:j+i]
                cnt = 1
        if cnt != 1:
            result += str(cnt) + temp_s
        else:
            result += temp_s

        answer.append(len(result))

    return min(answer)
