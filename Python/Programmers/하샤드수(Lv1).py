def solution(x):
    answer = True
    num = x
    sum_tmp = 0
    while True:
        if num < 10:
            sum_tmp += num
            break

        sum_tmp += num % 10
        num //= 10

    if x % sum_tmp:
        answer = False
    return answer