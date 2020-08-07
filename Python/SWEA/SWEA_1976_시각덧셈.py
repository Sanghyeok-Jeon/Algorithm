import sys
sys.stdin = open('1976.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))

    mm = (data[1]+data[3])%60
    hh = data[0]+data[2]+(data[1]+data[3])//60

    print('#{} {} {}'.format(tc+1, hh if hh < 13 else hh-12, mm))