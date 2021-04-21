def solution(N):
    answer = 0
    for i in range(1, N+1):
        if i*i > N:
            break
        elif i*i == N:
            answer += 1
            break
        else:
            if not N%i:
                answer += 2
    return answer