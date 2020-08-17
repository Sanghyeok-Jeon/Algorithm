def solution(n):
    answer = []
    data = str(n)
    for i in range(len(data)-1, -1 ,-1):
        answer.append(int(data[i]))
    return answer