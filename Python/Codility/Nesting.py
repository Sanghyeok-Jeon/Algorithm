def solution(S):
    if not len(S):
        return 1
    else:
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if len(stack):
                    stack.pop()
                else:
                    return 0
        if len(stack):
            return 0
        return 1