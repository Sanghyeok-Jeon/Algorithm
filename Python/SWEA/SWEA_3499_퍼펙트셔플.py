import sys
sys.stdin = open('3499.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(input().split())
    result = []

    if N % 2:
        for i in range(N//2):
            result.append(data[i])
            result.append(data[N//2 + i + 1])
        result.append(data[N//2])
    else:
        for i in range(N//2):
            result.append(data[i])
            result.append(data[i + N//2])

    print('#{}'.format(tc+1), end=' ')
    for i in range(N):
        print(result[i], end=' ')
    print()