import sys
sys.stdin = open('1221.txt', 'r')

T = int(input())

for tc in range(T):
    TC, n = map(str, input().split())
    N = int(n)
    data = list(map(str, input().split()))

    cnt_char = {}

    for i in range(len(data)):
        if data[i] in cnt_char:
            cnt_char[data[i]] += 1
        else:
            cnt_char[data[i]] = 1

    str_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    print(TC, end=' ')
    for i in range(10):
        for j in range(cnt_char[str_num[i]]):
            print(str_num[i], end=' ')
    print()