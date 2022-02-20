from itertools import permutations


def solution(numbers):
    answer = 0
    result = []

    for i in range(1, len(numbers) + 1):
        li = list(permutations(numbers, i))
        for j in li:
            a = int(''.join(j))
            if sosu(a):
                result.append(a)

    answer = len(set(result))

    return answer


def sosu(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
