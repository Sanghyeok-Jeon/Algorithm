import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i, N):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    print('#{}'.format(tc+1), end=' ')
    for i in range(N):
        print(data[i], end=' ')
    print()