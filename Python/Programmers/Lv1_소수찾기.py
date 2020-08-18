def solution(n):
    answer = 0
    num = [1, 1] + [0] * (n-1)
    for i in range(2, n+1):
        if not num[i]:
            answer += 1
            j = 1
            while i*j < n+1:
                if not num[i*j]:
                    num[i*j] = 1
                j += 1
    return answer