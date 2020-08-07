import sys
sys.stdin = open('1948.txt', 'r')

T = int(input())

for tc in range(T):
    days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    data = list(map(int, input().split()))

    between_days = 0
    start_month = data[0]
    end_month = data[2]

    if start_month == end_month:
        between_days += data[3] - data[1] + 1
    elif end_month - start_month == 1:
        between_days += data[3] + days_month[start_month] - data[1] + 1
    else:
        for i in range(1, end_month-start_month):
            between_days += days_month[start_month+i]
        between_days += data[3] + days_month[start_month] - data[1] + 1

    print('#{} {}'.format(tc+1, between_days))

