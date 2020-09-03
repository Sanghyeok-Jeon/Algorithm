import sys
sys.stdin = open('BOJ_14503.txt', 'r')

for _ in range(2):
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    print(room)