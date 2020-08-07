import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            died_flies = 0
            for x in range(M):
                for y in range(M):
                    died_flies += data[i+x][j+y]
            if died_flies > result:
                result = died_flies

    print('#{} {}'.format(tc+1, result))
