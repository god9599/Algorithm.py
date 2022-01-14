def solution(board, moves):
    li = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                li.append(board[j][i-1])
                board[j][i-1] = 0
                if len(li) > 1:
                    if li[-2] == li[-1]:
                        del li[-2]
                        del li[-1]
                        answer += 2
                break

    return answer
