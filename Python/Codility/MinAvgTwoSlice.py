def solution(A):
    minAvgSlice = (A[0] + A[1]) / 2
    minAvgIdx = 0
    for i in range(2, len(A)):
        tmpAvg = (A[i - 2] + A[i - 1] + A[i]) / 3
        if tmpAvg < minAvgSlice:
            minAvgSlice = tmpAvg
            minAvgIdx = i - 2

        tmpAvg = (A[i - 1] + A[i]) / 2
        if tmpAvg < minAvgSlice:
            minAvgSlice = tmpAvg
            minAvgIdx = i - 1

    return minAvgIdx