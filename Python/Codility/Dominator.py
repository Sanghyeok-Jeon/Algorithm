def solution(A):
    if not len(A):
        return -1

    dictCnt = {}
    maxCnt = 0
    maxValue = -1

    for a in A:
        if a in dictCnt:
            dictCnt[a] += 1
        else:
            dictCnt[a] = 1

        if dictCnt[a] > maxCnt:
            maxCnt = dictCnt[a]
            maxValue = a

    if maxCnt > len(A) // 2:
        for i, v in enumerate(A):
            if v == maxValue:
                return i
    else:
        return -1