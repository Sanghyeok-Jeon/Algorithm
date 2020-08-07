import sys
sys.stdin = open('1940.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    distance = 0
    v = 0
    for i in range(N):
        if data[i][0] == 0:
            distance += v
        elif data[i][0] == 1:
            v = data[i][1] + v
            distance += v
        else:
            v = v - data[i][1] if v - data[i][1] > 0 else 0
            distance += v

    print('#{} {}'.format(tc+1, distance))