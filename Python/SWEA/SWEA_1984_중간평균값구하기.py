import sys
sys.stdin = open('1984.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    N = 10
    for i in range(N-1):
        for j in range(i, N):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    result = round((sum(data)-data[0]-data[-1])/(N-2))

    print('#{} {}'.format(tc+1, result))