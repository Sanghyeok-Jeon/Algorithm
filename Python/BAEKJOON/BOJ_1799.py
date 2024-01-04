def dfs(n, cnt):    # n : 사선번호
    global ans
    # 가지치기 : 이대로 진행해도 정답 갱신 가능성 없는 경우 더 이상 진행 안함
    if ans >= (cnt + (L + 1 - n) // 2):    # 남은 자리 다 놓아도 정답 갱신 안되는 경우
        return

    if n >= L:
        ans = max(ans, cnt)
        return

    for ci, cj in diagonal[n]:    # 현재 사선번호에서 가능한 위치 하나씩 놓고 다음 사선으로
        if visited[ci-cj] == 0:    # 우하향 사선에 다른 비숍이 없는 경우(우하향 사선의 i-j는 일정하는 걸 이용)
            visited[ci-cj] = 1
            dfs(n+2, cnt+1)
            visited[ci-cj] = 0
    dfs(n+2, cnt)    # 이번 사선에서 안놓고 다음사선으로

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

diagonal = [[] for _ in range(N * 2)]
# diagonal[i][j] == 1인 경우, i+j 위치에 append (i+j 는 사선번호 - 우상향 사선의 i+j는 일정하다는 걸 이용)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:    # 비숍을 놓을 수 있는 자리인 경우
            diagonal[i+j].append((i, j))

L = 2 * N - 1    # 사선의 개수, 마지막 사선의 번호
visited = [0] * (2 * N)

# 체스판의 흑/백은 비숍이 상호간 이동 불가!
# 0부터 시작해서 2씩 증가 + 1부터 시작해서 2씩 증가
ans = 0
dfs(0, 0)    # 0부터 2씩 증가
t = ans
ans = 0
dfs(1, 0)    # 1부터 2씩 증가
print(ans + t)