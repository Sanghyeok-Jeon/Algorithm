def solution(A):
    answer = 0
    cntZero = 0
    for a in A:
        if a == 0:
            cntZero += 1
        else:
            answer += cntZero
            if answer > 1000000000:
                return -1
    return answer