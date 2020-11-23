import sys
sys.stdin = open('BOJ_3360.txt', 'r')

n = int(input())

dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i][0] = 1
    elif i == 2:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = 1
    elif i == 3:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-2][0] + dp[i-2][1]
        dp[i][2] = 1
    else:
        dp[i][0] = dp[i-1][0] % 1000000
        dp[i][1] = (dp[i-2][0] + dp[i-2][1]) % 1000000
        dp[i][2] = (dp[i-3][0] + dp[i-3][1] + dp[i-3][2]) % 1000000

print(sum(dp[n]) % 1000000)