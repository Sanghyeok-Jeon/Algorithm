def solution(A):
    sumPartOne = 0
    sumPartTwo = sum(A)
    answer = None

    for p in range(len(A)-1):
        sumPartOne += A[p]
        sumPartTwo -= A[p]

        diffSum = abs(sumPartOne - sumPartTwo)
        answer = min(diffSum, answer) if answer is not None else diffSum

    return answer