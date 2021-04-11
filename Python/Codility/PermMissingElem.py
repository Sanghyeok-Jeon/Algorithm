def solution(A):
    N = len(A)

    answer = (N + 1) * (N + 2) // 2
    for n in range(N):
        answer -= A[n]

    return answer