def solution(N):
    data = str(format(N, 'b'))

    maxGap = 0
    tmpGap = 0
    for d in data:
        if d == '1':
            maxGap = max(maxGap, tmpGap)
            tmpGap = 0
        elif d == '0':
            tmpGap += 1

    return maxGap