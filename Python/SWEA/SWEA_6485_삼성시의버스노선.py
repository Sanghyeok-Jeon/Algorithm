import sys
sys.stdin = open('6485.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    bus_line = []
    for _ in range(N):
        A, B = map(int, input().split())
        bus_line.append([A, B])
    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    count = [0] * 5001

    for i in range(N):
        for j in range(bus_line[i][0], bus_line[i][1]+1):
            count[j] += 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(P):
        print(count[C[i]], end=' ')
    print()