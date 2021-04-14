def solution(A, B, K):
    return B//K - A//K + (1 if not A%K else 0)