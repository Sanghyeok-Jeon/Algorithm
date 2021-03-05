import sys
sys.stdin = open('BOJ_11053.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))