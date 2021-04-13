def solution(A):
    A.sort()
    permCheck = 1
    answer = 1
    for a in A:
        if a != permCheck:
            answer = 0
            break
        permCheck += 1
    return answer