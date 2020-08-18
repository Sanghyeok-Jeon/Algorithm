def solution(a, b):
    answer = ''
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    tmp = b
    for i in range(1, a):
        tmp += days[i]

    answer = weekdays[(5 + tmp - 1) % 7]
    return answer