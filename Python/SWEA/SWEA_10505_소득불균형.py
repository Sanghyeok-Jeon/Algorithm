import sys
sys.stdin = open('10505.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    avg = sum(data) // N
    below_avg = 0
    for i in range(N):
        if data[i] <= avg:
            below_avg += 1

    print('#{} {}'.format(tc+1, below_avg))