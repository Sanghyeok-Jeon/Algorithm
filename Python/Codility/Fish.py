def solution(A, B):
    stackDown = []
    cntAlive = 0

    for i in range(len(A)):
        if B[i] == 1:
            stackDown.append(A[i])
        else:
            while len(stackDown):
                if stackDown[-1] > A[i]:
                    break
                else:
                    stackDown.pop()

        if not len(stackDown):
            cntAlive += 1

    return len(stackDown) + cntAlive