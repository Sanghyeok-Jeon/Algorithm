import sys
sys.stdin = open('1491.txt', 'r')

T = int(input())

for tc in range(T):
    N, A, B = map(int, input().split())
    min_result = 1000000000000

    for C in range(1, int(N**0.5) + 1):
        for R in range(C, N//C+1):
            temp = A * (R - C) + B * (N - R * C)
            if temp < min_result:
                min_result = temp

    print('#{} {}'.format(tc+1, min_result))