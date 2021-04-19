def solution(S):
    stack = []
    for s in S:
        if s == '{' or s == '(' or s == '[':
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            popStack = stack.pop()
            if popStack == '[':
                if s != ']':
                    return 0
            elif popStack == '(':
                if s != ')':
                    return 0
            else:
                if s != '}':
                    return 0

    if len(stack):
        return 0

    return 1