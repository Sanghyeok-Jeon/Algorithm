import sys
sys.stdin = open('1970.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count_money = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(8):
        count_money[i] = N//money[i]
        N %= money[i]

    print('#{}'.format(tc+1))
    for i in range(len(count_money)):
        print(count_money[i], end=' ')
    print()
