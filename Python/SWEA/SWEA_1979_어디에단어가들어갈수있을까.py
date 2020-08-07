import sys
sys.stdin = open('1979.txt', 'r')

def DFS1(i, j):
    global count, K, w_len
    if j == N:
        if w_len == K:
            count += 1
        w_len = 0
        return

    if data[i][j] == 0:
        if w_len == K:
            count += 1
        w_len = 0
        DFS1(i, j+1)
    else:
        w_len += 1
        DFS1(i, j+1)

def DFS2(j, i):
    global count, K, w_len
    if i == N:
        if w_len == K:
            count += 1
        w_len = 0
        return

    if data[i][j] == 0:
        if w_len == K:
            count += 1
        w_len = 0
        DFS2(j, i+1)
    else:
        w_len += 1
        DFS2(j, i+1)

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    w_len = 0

    for i in range(N):
        DFS1(i, 0)
        DFS2(i, 0)

    print('#{} {}'.format(tc+1, count))