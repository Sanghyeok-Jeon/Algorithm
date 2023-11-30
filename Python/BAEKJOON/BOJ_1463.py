import sys
sys.stdin = open('BOJ_1463.txt', 'r')

## dp 588ms
N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        if dp[i] > dp[i//2]:
            dp[i] = dp[i//2] + 1
    if i % 3 == 0:
        if dp[i] > dp[i//3]:
            dp[i] = dp[i//3] + 1

print(dp[N])

## 984ms
# def DFS(n, cnt):
#     global min_cnt
#     if n == 1:
#         min_cnt = min(min_cnt, cnt)
#         return
#
#     if cnt >= min_cnt:
#         return
#
#     if n % 3 == 0:
#         DFS(n//3, cnt+1)
#     if n % 2 == 0:
#         DFS(n//2, cnt+1)
#     DFS(n-1, cnt+1)
#
# for _ in range(2):
#     N = int(input())
#     min_cnt = N
#
#     DFS(N, 0)
#
#     print(min_cnt)