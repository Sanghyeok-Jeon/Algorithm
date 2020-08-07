import sys
sys.stdin = open('3142.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    # unicorn = x, twinhorn = y 라면
    # N(총 뿔의 수) = x + 2y
    # M(총 마리수) = x + y

    unicorn = 2 * M - N
    twinhorn = N - M

    print('#{} {} {}'.format(tc+1, unicorn, twinhorn))