import sys
sys.stdin = open('SWEA_11315.txt', 'r')

def checkDirection(i, j, mode):
    tempPossible = True
    cnt = 1
    while True:
        if cnt >= 5:
            break
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
            cnt += 1
        else:
            tempPossible = False
            break
        i, j = ni, nj
    if cnt < 5:
        tempPossible = False
    return tempPossible

def check(i, j):
    tempPossible = False
    for mode in range(5):
        tempPossible = checkDirection(i, j, mode)
        if tempPossible:
            return tempPossible
    return tempPossible

T = int(input())
for tc in range(T):
    N = int(input())
    board = [input() for _ in range(N)]

    di = [0, 1, 1, 1, 0]
    dj = [1, 1, 0, -1, -1]

    possible = False
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                possible = check(i, j)
                if possible:
                    break
        if possible:
            break

    if possible:
        print('#{} {}'.format(tc+1, 'YES'))
    else:
        print('#{} {}'.format(tc+1, 'NO'))