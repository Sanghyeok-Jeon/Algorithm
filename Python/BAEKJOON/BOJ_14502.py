from collections import deque
import copy

# 연구소에 벽을 세우는 함수
def build_wall(count):
    global max_safe_area

    if count == 3:
        temp_lab = copy.deepcopy(lab)  # 연구소 복사
        spread_virus(temp_lab)  # 바이러스 확산
        safe_area = count_safe_area(temp_lab)   # 안전 영역 계산
        max_safe_area = max(max_safe_area, safe_area)   # 최대 안전 영역 비교

        return
    
    # 벽 세우기
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build_wall(count + 1)
                lab[i][j] = 0

# 바이러스 확산
def spread_virus(temp_lab):
    q = deque()
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]
            if 0 <= nx < N and 0 <= ny < M and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                q.append((nx, ny))

# 안전 영역 계산
def count_safe_area(temp_lab):
    count = 0
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 0:
                count += 1

    return count

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 안전 영역 크리 초기화
max_safe_area = 0

# 벽 세우기
build_wall(0)

print(max_safe_area)