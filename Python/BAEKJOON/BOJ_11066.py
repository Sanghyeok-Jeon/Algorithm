T = int(input())
for _ in range(T):
    K = int(input())
    data = list(map(int, input().split()))

    # 파일 크기의 합을 미리 계산
    S = [0]
    for d in data:
        S.append(S[-1] + d)

    # 파일을 합치는데 필요한 최소 비용 계산
    dp = [[0]*K for _ in range(K)]
    for size in range(1, K):
        for i in range(K - size):
            j = i + size
            dp[i][j] = float('inf')

            # i부터 j까지의 파일을 합치는 모든 경우를 탐색
            for k in range(i, j):
                # (i부터 k까지의 파일을 합치는 비용) + (k+1부터 j까지의 파일을 합치는 비용) + (i부터 j까지의 파일 크기의 합)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + S[j+1] - S[i])

    print(dp[0][K-1])
