def solution(A):
    missingInteger = 1
    A.sort()
    for a in A:
        if a == missingInteger and a > 0:
            missingInteger += 1
    return missingInteger