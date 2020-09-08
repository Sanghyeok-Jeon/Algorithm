import sys
sys.stdin = open('SWEA_1226.txt', 'r')

def DFS(i, j):
    global possible, end_i, end_j
    if i == end_i and j == end_j:
        possible = 1
        return

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and (maze[ni][nj] == '0' or maze[ni][nj] == '3'):
            visited[ni][nj] = 1
            DFS(ni, nj)

for tc in range(10):
    n = int(input())
    maze = [input() for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    start_i, start_j = 0, 0
    end_i, end_j = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start_i = i
                start_j = j
            if maze[i][j] == '3':
                end_i = i
                end_j = j

    possible = 0
    visited[1][1] = 1
    DFS(start_i, start_j)

    print('#{} {}'.format(tc+1, possible))