import sys
sys.stdin = open('BOJ_14501.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    dp = [0] * 21

    for i in range(1, N+1):
        T, P = map(int, input().split())
        dp[i+1] = max(dp[i], dp[i+1])  # 이전까지의 페이가 더 높으면 건너뛴다
        if i + T <= N+1:
            dp[i + T] = max(dp[i] + P, dp[i + T])

    print(max(dp))
