import sys
sys.stdin = open('5789.txt', 'r')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    data = []
    for i in range(Q):
        L, R = map(int, input().split())
        data.append([L, R, i+1])

    for i in range(Q):
        for j in range(data[i][0], data[i][1]+1):
            box[j] = data[i][2]

    print('#{}'.format(tc+1), end=' ')
    for i in range(1, N+1):
        print(box[i], end=' ')
    print()