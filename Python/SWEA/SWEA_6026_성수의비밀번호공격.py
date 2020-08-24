import sys
sys.stdin = open('SWEA_6026.txt', 'r')

def comb(i):
    global N, M
    n = 1
    for j in range(i):
        n *= (M-j)
        n //= j+1
    return n

T = int(input())

for tc in range(T):
    M, N = map(int, input().split())
    dp = [0] * M
    for i in range(1, M):
        dp[i] = comb(i) * i**N - dp[i-1]

    print('#{} {}'.format(tc+1, (M**N - dp[M-1]) % 1000000007))