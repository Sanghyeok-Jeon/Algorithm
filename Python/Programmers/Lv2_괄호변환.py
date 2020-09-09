def seperate(w):
    openBracket = 0
    closeBracket = 0

    for i in range(len(w)):
        if w[i] == '(':
            openBracket += 1
        else:
            closeBracket += 1

        if openBracket == closeBracket:
            return w[:i + 1], w[i + 1:]


def balanceCheck(u):
    bracket = []
    for s in u:
        if s == '(':
            bracket.append(s)
        else:
            if not len(bracket):
                return 0
            bracket.pop()
    return 1


def solution(w):
    if not len(w):
        return w

    u, v = seperate(w)

    if balanceCheck(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'

        for s in u[1:len(u) - 1]:
            if s == '(':
                result += ')'
            else:
                result += '('

        return result