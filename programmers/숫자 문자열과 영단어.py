def solution(s):
    num_dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    temp = ''
    answer = ' '
    for word in s:
        if word.isdigit():
            answer += word
        elif word.isalpha():
            temp += word
            if temp in num_dic.keys():
                answer += num_dic[temp]
                temp = ''
    print(int(answer))
    return int(answer)
