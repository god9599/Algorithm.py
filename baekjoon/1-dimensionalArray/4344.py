import sys

n = int(sys.stdin.readline())

student_list = list()
for i in range(n):
    student_list.append(list(map(int, input().split(' '))))

for j in student_list:
    num_of_student = j[0]
    avg = sum(j[1:]) / num_of_student
    count = 0
    for score in j[1:]:
        if(avg < score):
            count += 1
    print('%.3f' % ((count / num_of_student) * 100) + '%')



