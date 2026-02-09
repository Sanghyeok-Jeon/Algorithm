import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

# 최대 비용
max_cost = sum(C)

# dp[i][j] : i번째 앱까지 고려했을때, j 비용으로 확보할 수 있는 최대 메모리
dp = [[0] * (max_cost + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    memory = A[i]
    cost = C[i]
    for j in range(max_cost + 1):
        if cost <= j:    # 앱 끈 뒤의 메모리와 그렇지 않을 때의 메모리중 큰 값을 입력
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + memory)
        else:    # 현재 앱의 cost가 j보다 크면 끄지 않고 활성화상태로 둔다. 
            dp[i][j] = dp[i - 1][j]

# 최소 비용 찾기
min_cost = max_cost
for j in range(max_cost + 1):
    if dp[N][j] >= M:
        min_cost = j
        break

print(min_cost)