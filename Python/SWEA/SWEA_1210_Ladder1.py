import sys
sys.stdin = open('SWEA_1210.txt', 'r')

def DFS(i, j, start, direction):
    global X
    if i == 99:
        if ladder[i][j] == 2:
            X = start
        return

    change = 0
    if direction == 0:
        for mode in range(1, 3):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < 100 and 0 <= nj < 100 and ladder[ni][nj] == 1:
                DFS(ni, nj, start, mode)
                change = 1
                break

        if change == 0:
            DFS(i+1, j, start, direction)
    else:
        ni = i + di[0]
        nj = j + dj[0]
        if 0 <= ni < 100 and 0 <= nj < 100:
            if ladder[ni][nj] == 1:
                DFS(ni, nj, start, 0)
            else:
                DFS(i, j + dj[direction], start, direction)

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [1, 0, 0]
    dj = [0, 1, -1]

    direction = 0
    X = -1
    for j in range(100):
        if ladder[0][j]:
            visited = [[0] * 100 for _ in range(100)]
            DFS(0, j, j, 0)

    print('#{} {}'.format(tc, X))