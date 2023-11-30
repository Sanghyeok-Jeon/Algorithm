import sys
sys.stdin = open('BOJ_15651.txt', 'r')

def DFS(cnt):
    if cnt == M:
        print(*ans)
        return

    for i in range(1, N+1):
        ans.append(i)
        DFS(cnt+1)
        ans.pop()

N, M = map(int, input().split())

ans = []
DFS(0)