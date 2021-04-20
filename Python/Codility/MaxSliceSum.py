def solution(A):
    if len(A) == 1:
        return A[0]

    nowMaxSum = A[0]
    maxSum = A[0]

    for i in range(1, len(A)):
        nowMaxSum = max(A[i], nowMaxSum + A[i])
        maxSum = max(maxSum, nowMaxSum)

    return maxSum