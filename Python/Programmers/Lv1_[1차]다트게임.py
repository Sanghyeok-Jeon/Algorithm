def solution(dartResult):
    answer = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    cnt_num = 0
    i = 0
    while True:
        if cnt_num == 3:
            break

        if dartResult[i] in numbers:
            if dartResult[i + 1] in numbers:
                answer.append(int(dartResult[i:i + 2]))
                i += 2
            else:
                answer.append(int(dartResult[i]))
                i += 1

            if dartResult[i] == 'D':
                answer[-1] = answer[-1] ** 2
            elif dartResult[i] == 'T':
                answer[-1] = answer[-1] ** 3
            i += 1

            if i >= len(dartResult):
                break

            if dartResult[i] == '*':
                answer[-1] *= 2
                if len(answer) > 1:
                    answer[-2] *= 2
                i += 1
            elif dartResult[i] == '#':
                answer[-1] *= -1
                i += 1
            else:
                cnt_num += 1
                continue

        cnt_num += 1

    return sum(answer)