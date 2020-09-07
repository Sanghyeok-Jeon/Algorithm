import sys
sys.stdin = open('SWEA_7465.txt', 'r')

def grouping(i):
    for j in know[i]:
        if visited[j] == 0:
            visited[j] = 1
            grouping(j)

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    know = [[] for _ in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        know[p1].append(p2)
        know[p2].append(p1)
    visited = [0] * (N+1)

    group = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            group += 1
            visited[i] = 1
            grouping(i)

    print('#{} {}'.format(tc+1, group))

