def solution(A):
    cntElement = {}
    for a in A:
        if a in cntElement:
            cntElement[a] += 1
        else:
            cntElement[a] = 1

    answer = 0
    for key, value in cntElement.items():
        if value % 2:
            answer = key

    return answer