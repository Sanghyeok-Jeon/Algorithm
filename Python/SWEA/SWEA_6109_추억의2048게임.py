import sys
sys.stdin = open('SWEA_6109.txt', 'r')

T = int(input())

for tc in range(T):
    n, direction = input().split()
    N = int(n)
    board = [list(map(int, input().split())) for _ in range(N)]
    fixed = [[0]*N for _ in range(N)]

    if direction == 'up':
        for j in range(N):
            i = 0
            while i < N-1:
                if i == 0:
                    for _ in range(N):
                        if board[i][j] == 0:
                            for k in range(i, N-1):
                                board[k][j], board[k+1][j] = board[k+1][j], 0
                        else:
                            i += 1
                    i = 0
                if board[i][j] == board[i+1][j]:
                    board[i][j] *= 2
                    for k in range(i+1, N-1):
                        board[k][j] = board[k+1][j]
                    board[N-1][j] = 0
                i += 1

    elif direction == 'down':
        for j in range(N):
            i = N-1
            while i > 0:
                if i == N-1:
                    for _ in range(N):
                        if board[i][j] == 0:
                            for k in range(i, 0, -1):
                                board[k][j], board[k-1][j] = board[k-1][j], 0
                        else:
                            i -= 1
                    i = N-1
                if board[i][j] == board[i-1][j]:
                    board[i][j] *= 2
                    for k in range(i-1, 0, -1):
                        board[k][j] = board[k-1][j]
                    board[0][j] = 0
                i -= 1

    elif direction == 'left':
        for i in range(N):
            j = 0
            while j < N-1:
                if j == 0:
                    for _ in range(N):
                        if board[i][j] == 0:
                            for k in range(j, N-1):
                                board[i][k], board[i][k+1] = board[i][k+1], 0
                        else:
                            j += 1
                    j = 0
                if board[i][j] == board[i][j+1]:
                    board[i][j] *= 2
                    for k in range(j+1, N-1):
                        board[i][k] = board[i][k+1]
                    board[i][N-1] = 0
                j += 1

    else:
        for i in range(N):
            j = N-1
            while j > 0:
                if j == N-1:
                    for _ in range(N):
                        if board[i][j] == 0:
                            for k in range(j, 0, -1):
                                board[i][k], board[i][k-1] = board[i][k-1], 0
                        else:
                            j -= 1
                    j = N-1
                if board[i][j] == board[i][j-1]:
                    board[i][j] *= 2
                    for k in range(j-1, 0, -1):
                        board[i][k] = board[i][k-1]
                    board[i][0] = 0
                j -= 1

    print('#{}'.format(tc+1))
    for i in range(N):
        print(*board[i], sep=' ')