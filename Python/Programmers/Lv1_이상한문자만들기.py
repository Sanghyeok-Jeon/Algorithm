def solution(s):
    data = list(s)

    cnt = 0
    for i in range(len(data)):
        if data[i] == ' ':
            cnt = 0
        else:
            if cnt % 2 == 0:
                data[i] = data[i].upper()
            else:
                data[i] = data[i].lower()
            cnt += 1

    answer = ''.join(data)
    return answer