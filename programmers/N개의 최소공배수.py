def solution(arr):
    answer = 0
    arr.sort()
    arr.reverse()

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            answer = arr[0]
            break

    return answer


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)
