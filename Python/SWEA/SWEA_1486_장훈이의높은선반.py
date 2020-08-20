import sys
sys.stdin = open('SWEA_1486.txt', 'r')

def DFS(cnt, tmpH):
    global N, min_H, B
    if cnt == N:
        if tmpH < min_H and tmpH >= B:
            min_H = tmpH
        return

    DFS(cnt+1, tmpH+Hi[cnt])
    DFS(cnt+1, tmpH)


T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))
    min_H = 10000 * N

    DFS(0, 0)

    print('#{} {}'.format(tc+1, min_H-B))