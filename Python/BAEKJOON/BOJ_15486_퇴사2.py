import sys
sys.stdin = open('BOJ_15486.txt', 'r')

for i in range(4):
    N = int(input())
    dp = [0] * (N + 2)

    for i in range(1, N + 1):
        T, P = map(int, sys.stdin.readline().split())

        if dp[i] > dp[i + 1]:
            dp[i + 1] = dp[i]

        if i + T <= N + 1:
            dp[i + T] = max(dp[i + T], dp[i] + P)

    print(max(dp))