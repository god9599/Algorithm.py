def solution(n, a, b):
    answer = 0

    while not a == b:
        if a % 2 == 0:
            a = a // 2
        elif not a % 2 == 0:
            a = a // 2 + 1
        if b % 2 == 0:
            b = b // 2
        elif not b % 2 == 0:
            b = b // 2 + 1

        answer += 1

    return answer
