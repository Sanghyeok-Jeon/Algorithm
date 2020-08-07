import sys
sys.stdin = open('1220.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    couple_magnet = 0

    for j in range(N):
        n = 0
        s = 0
        for i in range(N):
            if magnetic[i][j] == 1:
                n = 1

            if n == 1:
                if magnetic[i][j] == 2:
                    s = 1

            if n == 1 and s == 1:
                couple_magnet += 1
                n = s = 0

    print('#{} {}'.format(tc+1, couple_magnet))