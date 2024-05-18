from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    q = deque()
    q.append((x, y, cnt))
    visited[x][y] = 1    # 시작점 방문 체크
    max_value = -1

    while q:
        x, y, cnt = q.popleft()

        if max_value < cnt:
            max_value = cnt

        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]
            if 0 <= nx < N and 0 <= ny < M:
                if treasure_map[nx][ny] == 'L' and visited[nx][ny] == 0:     # 아직 방문하지 않은 땅이라면
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1

    return max_value    # 최대 거리 반환 (시작점 1 차감)

N, M = map(int, input().split())
treasure_map = [list(input()) for _ in range(N)]    # 보물섬 지도
result = -1

for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':    # 땅인 경우
            visited = [[0] * M for _ in range(N)]
            result = max(result, bfs(i, j, 0))

print(result)