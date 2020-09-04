def solution(N, stages):
    answer = {}
    challenger = len(stages)

    for i in range(1, N + 1):
        answer[i] = stages.count(i) / challenger if challenger else 0
        challenger -= stages.count(i)

    return sorted(answer, key=lambda x: answer[x], reverse=True)