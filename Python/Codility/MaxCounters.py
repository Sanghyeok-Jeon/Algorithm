def solution(N, A):
    counter = [0] * N
    maxCounter = 0
    lastMaxCounter = 0

    for K in range(len(A)):
        if A[K] == N + 1:
            lastMaxCounter = maxCounter
        else:
            counter[A[K] - 1] = max(lastMaxCounter, counter[A[K] - 1])
            counter[A[K] - 1] += 1
            maxCounter = max(maxCounter, counter[A[K] - 1])

    for i in range(N):
        counter[i] = max(lastMaxCounter, counter[i])

    return counter
