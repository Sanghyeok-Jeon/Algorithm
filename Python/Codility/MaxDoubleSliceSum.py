def solution(A):
    if len(A) <= 3:
        return 0

    sumLeft = [0] * len(A)
    sumRight = [0] * len(A)

    for i in range(1, len(A) - 1):
        sumLeft[i] = max(0, sumLeft[i - 1] + A[i])

    for i in range(len(A) - 2, 1, -1):
        sumRight[i] = max(0, sumRight[i + 1] + A[i])

    maxSum = 0
    for i in range(1, len(A) - 1):
        maxSum = max(maxSum, sumLeft[i - 1] + sumRight[i + 1])

    return maxSum