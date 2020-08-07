import sys
sys.stdin = open('1860.txt', 'r')

T = int(input())
result = []

for tc in range(T):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))

    customer = [0] * 11112
    maxTime = -1
    for i in range(N):
        customer[data[i]] += 1
        if data[i] > maxTime:
            maxTime = data[i]

    needBread = [0] * (maxTime+1)
    accumulate_need = 0
    for i in range(maxTime+1):
        if customer[i]:
            needBread[i] = accumulate_need + customer[i]
            accumulate_need += customer[i]

    fishBread = [0] * (11112+M)
    accumulate_bread = 0
    for i in range(M, 11112, M):
        accumulate_bread += K
        for j in range(i, i+M):
            fishBread[j] = accumulate_bread

    impossible = 0
    for i in range(len(needBread)):
        if fishBread[i] < needBread[i]:
            impossible = 1
            break

    result.append('Impossible' if impossible else 'Possible')

x = 1
for i in range(T):
    print('#{} {}'.format(x, result[i]))
    x += 1