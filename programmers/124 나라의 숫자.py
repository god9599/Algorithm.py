def solution(n):
    answer = ''
    while n:
        if n % 3 != 0: # n이 3으로 나누어떨어지지 않을 때
            answer += str(n % 3)
            n //= 3 
        elif n % 3 == 0: # 나누어 떨어질 때
            answer += "4"
            n = n // 3 - 1
    
    return answer[::-1]
