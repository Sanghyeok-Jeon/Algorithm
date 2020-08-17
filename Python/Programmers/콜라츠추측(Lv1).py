def solution(num):
    answer = 0

    cnt = 0
    while cnt < 500:
        if num == 1:
            answer = cnt
            break

        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2

        cnt += 1

    if num > 1:
        answer = -1

    return answer