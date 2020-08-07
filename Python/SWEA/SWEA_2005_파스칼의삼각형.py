import sys
sys.stdin = open('2005.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    data = [[0] * N for _ in range(N)]
    data[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                data[i][j] = 1
            else:
                data[i][j] = data[i-1][j-1] + data[i-1][j]

    print('#{}'.format(tc+1))
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                print(data[i][j], end=' ')
        print()
