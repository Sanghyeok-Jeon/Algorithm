def solution(info, query):
    challenger = []
    for i in range(len(info)):
        challenger.append(info[i].split(' '))

    condition = []
    for i in range(len(query)):
        tmp_query = query[i].split(' ')
        for j in range(3):
            tmp_query.remove('and')
        condition.append(tmp_query)

    possible = [0] * len(condition)
    for i in range(len(challenger)):
        for j in range(len(condition)):
            break_point = 0
            for k in range(4):
                if challenger[i][k] == condition[j][k] or condition[j][k] == '-':
                    continue
                else:
                    break_point = 1
                    break

            if break_point == 0:
                if int(challenger[i][4]) >= int(condition[j][4]):
                    possible[j] += 1

    return possible