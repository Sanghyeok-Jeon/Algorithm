def solution(arr, divisor):
    answer = []
    element = 0
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
            element += 1
    if element == 0:
        answer.append(-1)
    answer.sort()
    return answer