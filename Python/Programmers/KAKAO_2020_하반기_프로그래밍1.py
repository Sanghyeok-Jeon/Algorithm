def solution(new_id):
    new_id = new_id.lower()

    data = list(new_id)

    tmp_cnt = 0
    for i in range(len(data)):
        if data[i].isalpha() or data[i].isdigit() or data[i] == '-' or data[i] == '_' or data[i] == '.':
            continue
        else:
            data[i] = '#'
            tmp_cnt += 1

    for i in range(tmp_cnt):
        data.remove('#')

    new_id = ''.join(data)

    tmp_id = ''
    for i in new_id:
        if i == '.':
            if len(tmp_id) and tmp_id[-1] == '.':
                continue
            else:
                tmp_id += i
        else:
            tmp_id += i

    data = list(tmp_id)

    tmp_cnt = 0
    for i in range(len(data)):
        if data[i] == '.':
            tmp_cnt += 1
        else:
            break
    for i in range(tmp_cnt):
        data.remove('.')

    tmp_cnt = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] == '.':
            tmp_cnt += 1
        else:
            break
    for i in range(tmp_cnt):
        data.pop()

    if len(data) == 0:
        data.append('a')

    if len(data) > 15:
        del data[15:]

    tmp_cnt = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] == '.':
            tmp_cnt += 1
        else:
            break
    for i in range(tmp_cnt):
        data.pop()

    if len(data) < 3:
        while len(data) < 3:
            data.append(data[-1])

    answer = ''.join(data)

    return answer