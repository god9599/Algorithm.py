def solution(n, arr1, arr2):
    li = []
    for i, j in zip(arr1, arr2):
        list1 = int(bin(i)[2:])
        list2 = int(bin(j)[2:])
        li.append(str(list1+list2).zfill(n))
    fin = []
    for a in li:
        string = ''
        for b in a:
            if b == '0':
                string += " "
            else:
                string += "#"
        fin.append(string)
    return fin
