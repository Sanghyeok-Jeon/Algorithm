import sys
sys.stdin = open('SWEA_1211.txt', 'r')

def DFS(i, j, start, direction, distance):
    global X, min_distance
    if i == 99:
        if min_distance > distance:
            min_distance = distance
            X = start
        return

    if direction == 2:
        for mode in range(3):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if ladder[ni][nj] == 1:
                    DFS(ni, nj, start, mode, distance+1)
                    break
    else:
        ni = i + di[2]
        nj = j + dj[2]
        if 0 <= ni < 100 and 0 <= nj < 100:
            if ladder[ni][nj] == 1:
                DFS(ni, nj, start, 2, distance+1)
            else:
                DFS(i, j+dj[direction], start, direction, distance+1)

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [0, 0, 1]
    dj = [-1, 1, 0]

    X = -1
    min_distance = 100 * 100
    for j in range(100):
        if ladder[0][j] == 1:
            DFS(0, j, j, 2, 1)

    print('#{} {}'.format(tc, X))