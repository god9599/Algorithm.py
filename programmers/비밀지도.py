def solution(n, arr1, arr2):
    answer = []

    dec1 = decrypt(n, arr1)
    dec2 = decrypt(n, arr2)
    for _dec1, _dec2 in zip(dec1, dec2):
        result = ''
        for j in range(n):
            if _dec1[j] == 1 or _dec2[j] == 1:
                result += '#'
            elif _dec1[j] == 0 and _dec2[j] == 0:
                result += ' '
        answer.append(result)
    return answer


def decrypt(n, arr):
    decrypt_list = []
    for i in arr:
        li = []
        while True:
            li.append(i % 2)
            i = i // 2
            if i == 0:
                if len(li) < n:
                    for i in range(1, n - len(li) + 1):
                        li.append(0)
                break
        li.reverse()
        decrypt_list.append(li)
    return decrypt_list
