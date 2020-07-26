import sys
sys.stdin = open('4371.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(int(input()))
    ships = 0

    ship = 0
    for i in range(1, N):
        if data[i]:
            ship = data[i] - 1
            ships += 1
        for j in range(i+1, N):
            if (data[j]-1) % ship == 0:
                data[j] = 0

    print('#{} {}'.format(tc+1, ships))
