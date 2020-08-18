def solution(brown, yellow):
    answer = []
    b, y = brown, yellow
    dataY = []

    for i in range(1, int(y ** 0.5) + 1):
        if not y % i:
            dataY.append([y // i, i])

    for i in range(len(dataY)):
        if (dataY[i][0] + dataY[i][1]) * 2 + 4 == b:
            answer = [dataY[i][0] + 2, dataY[i][1] + 2]

    return answer