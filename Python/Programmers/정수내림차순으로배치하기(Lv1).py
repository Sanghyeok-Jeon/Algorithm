def solution(n):
    answer = 0
    data = list(str(n))
    data.sort(reverse=True)
    answer = int(''.join(data))
    return answer