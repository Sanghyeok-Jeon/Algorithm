import sys
sys.stdin = open('BOJ_14501.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * 20

    for i in range(N):
        if dp[i] > dp[i+1]:
            dp[i+1] = dp[i]

        if dp[i + data[i][0]] < dp[i] + data[i][1]:
            dp[i + data[i][0]] = dp[i] + data[i][1]

    print(dp[N])