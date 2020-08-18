def solution(s):
    S = list(s)
    answer = ''.join(sorted(S, key=lambda x: ord(x))[::-1])

    return answer