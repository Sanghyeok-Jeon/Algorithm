def solution(A, K):
    N = len(A)
    if N:
        return A[N-K%N:] + A[:N-K%N]
    else:
        return A