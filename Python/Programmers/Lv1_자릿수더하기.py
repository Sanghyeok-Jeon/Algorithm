def solution(n):
    answer = 0

    data = str(n)
    for s in data:
        answer += int(s)

    return answer