import sys
sys.stdin = open('SWEA_11387.txt', 'r')

T = int(input())
for tc in range(T):
    D, L, N = map(int, input().split())
    ans = D * N + D * N * (N-1) * 0.5 * L * 0.01
    print('#{} {}'.format(tc+1, int(ans)))