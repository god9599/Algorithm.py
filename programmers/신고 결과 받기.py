def solution(id_list, report, k):
    answer = []
    reported_by = []  # 신고 당한 사람 리스트
    pause_user = []  # 정지 당한 사람 리스트
    report = list(set(report))
    for i in report:
        reported_by.append(i.split()[1])

    for j in id_list:
        if reported_by.count(j) >= k:
            pause_user.append(j)

    for a in id_list:
        cnt = 0
        for b in report:
            if b.split()[1] in pause_user and a == b.split()[0]:
                cnt += 1
        answer.append(cnt)

    return answer
