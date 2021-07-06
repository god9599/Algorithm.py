answers = [1, 2, 3, 4, 5]


def solution(answers):
    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0 for i in range(3)]  # [0, 0, 0]

    for i in range(len(answers)):
        if(answers[i] == answer1[i % 5]):
            score[0] += 1
        if(answers[i] == answer2[i % 8]):
            score[1] += 1
        if(answers[i] == answer3[i % 10]):
            score[2] += 1
    answer = []
    max = 0

    for i in range(3):
        if max < score[i]:
            max = score[i]
            answer = [i+1]
        elif max == score[i]:
            answer.append(i+1)

    return answer


print(solution(answers))
