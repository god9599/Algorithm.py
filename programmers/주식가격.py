def solution(prices):
    stack = [0]
    cnt = len(prices)
    answer = [i for i in range(len(prices)-1, -1, -1)]
    
    for i in range(1, cnt):
        while stack and prices[stack[-1]] > prices[i]:
            time = stack.pop()
            answer[time] = i - time
        
        stack.append(i)
    
    return answer