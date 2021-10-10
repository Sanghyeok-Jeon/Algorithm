import sys
sys.stdin = open('SWEA_11736.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    answer = 0
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(1, N-1):
        a, b, c = data[i-1], data[i], data[i+1]
        if b != max(a, b, c) and b != min(a, b, c):
            answer += 1

    print('#{} {}'.format(tc, answer))