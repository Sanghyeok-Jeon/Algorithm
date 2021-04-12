def solution(X, A):
    leaves = set()
    answer = -1
    for K in range(len(A)):
        leaves.add(A[K])
        if len(leaves) == X:
            answer = K
            break
    return answer