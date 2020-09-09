def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    lst_str1 = []
    lst_str2 = []

    for i in range(len(str1) - 1):
        if (str1[i] + str1[i + 1]).isalpha():
            lst_str1.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if (str2[i] + str2[i + 1]).isalpha():
            lst_str2.append(str2[i] + str2[i + 1])

    if not len(lst_str1) + len(lst_str2):
        return 65536

    same = 0
    for ss in lst_str1:
        if ss in lst_str2:
            lst_str2.remove(ss)
            same += 1

    return int(same / (len(lst_str1) + len(lst_str2)) * 65536)