import sys
sys.stdin = open('5603.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    gunchos = []
    sum_gunchos = 0
    for _ in range(N):
        guncho = int(input())
        gunchos.append(guncho)
        sum_gunchos += guncho

    average_gunchos = sum_gunchos // N
    move_guncho = 0
    for i in range(N):
        move_guncho += abs(gunchos[i] - average_gunchos)

    print('#{} {}'.format(tc+1, move_guncho//2))