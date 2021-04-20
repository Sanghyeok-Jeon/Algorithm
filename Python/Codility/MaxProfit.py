def solution(A):
    if len(A) < 2:
        return 0

    maxProfit = 0
    minProfit = A[0]
    for a in A[1:]:
        tmpProfit = a - minProfit
        if tmpProfit > 0:
            maxProfit = max(maxProfit, tmpProfit)
        else:
            minProfit = a

    return maxProfit