def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[len(A)-1], A[len(A)-3]*A[len(A)-2]*A[len(A)-1])