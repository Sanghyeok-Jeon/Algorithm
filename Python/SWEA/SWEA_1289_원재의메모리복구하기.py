import sys
sys.stdin = open('1289.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()
    cnt_revise = 0

    now_bit = '0'
    i = 0
    while i < len(data):
        if data[i] != now_bit:
            cnt_revise += 1
            now_bit = data[i]
        i += 1

    print('#{} {}'.format(tc+1, cnt_revise))