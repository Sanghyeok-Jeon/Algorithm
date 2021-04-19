def solution(H):
    stack = []
    cntWall = 0

    for h in H:
        while len(stack) and stack[-1] > h:
            stack.pop()

        if not len(stack) or stack[-1] < h:
            stack.append(h)
            cntWall += 1

    return cntWall