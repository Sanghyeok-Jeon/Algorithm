def solution(array, commands):
    answer = []
    for z in range(len(commands)):
        i, j, k = commands[z][0], commands[z][1], commands[z][2]
        tmp = sorted(array[i-1:j])[k-1]
        answer.append(tmp)
    return answer