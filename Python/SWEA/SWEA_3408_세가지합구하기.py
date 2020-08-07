import sys
sys.stdin = open('3408.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    S1 = N * (N+1) // 2
    S3 = S1 * 2
    S2 = S3 - N

    print('#{} {} {} {}'.format(tc+1, S1, S2, S3))