import sys
sys.stdin = open('5515.txt', 'r')

T = int(input())

for tc in range(T):
    m, d = map(int, input().split())
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = d
    for i in range(1, m):
        days += month_days[i]

    weekday = 4 + days % 7 - 1

    print('#{} {}'.format(tc+1, weekday if weekday < 7 else weekday-7))
