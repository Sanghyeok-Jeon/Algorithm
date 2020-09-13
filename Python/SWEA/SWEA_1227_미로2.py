import sys
sys.stdin = open('SWEA_1227.txt')
import collections

def BFS():
    global possible

    while q:
        i, j = q.popleft()
        maze[i][j] = '1'
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]
            if maze[ni][nj] == '3':
                possible = 1
                return
            if 0 <= ni < 100 and 0 <= nj < 100 and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                q.append((ni, nj))

for _ in range(10):
    tc = int(input())
    maze = [list(input()) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]

    start_i, start_j = 0, 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                start_i, start_j = i, j

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    possible = 0

    q = collections.deque()
    q.append((start_i, start_j))

    BFS()

    print('#{} {}'.format(tc, possible))

