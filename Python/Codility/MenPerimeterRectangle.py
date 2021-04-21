def solution(N):
    for i in range(int(N**0.5), 0, -1):
        if not N%i:
            return 2 * (i + N//i)