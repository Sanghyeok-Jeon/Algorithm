import sys
sys.stdin = open('3456.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    cnt_num = [0] * 101

    for i in range(3):
        cnt_num[data[i]] += 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(101):
        if cnt_num[i] % 2:
            print(i)
