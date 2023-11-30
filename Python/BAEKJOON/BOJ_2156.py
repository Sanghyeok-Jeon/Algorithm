import sys
sys.stdin = open('BOJ_2156.txt', 'r')

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = wine[1]
    elif i == 2:
        dp[i] = wine[1] + wine[2]
    else:
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[n])