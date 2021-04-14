def solution(S, P, Q):
    answer = []
    for i in range(len(P)):
        tmpS = S[P[i]:Q[i]+1]
        if 'A' in tmpS:
            answer.append(1)
        elif 'C' in tmpS:
            answer.append(2)
        elif 'G' in tmpS:
            answer.append(3)
        else:
            answer.append(4)
    return answer