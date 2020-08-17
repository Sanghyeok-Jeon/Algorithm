import sys
sys.stdin = open('SWEA_10580.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    pole = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    pole.sort(key=lambda x: x[0])
    cnt = 0

    for i in range(N):
        target = pole[i][1]
        for j in range(i+1, N):
            if pole[j][1] < target:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))