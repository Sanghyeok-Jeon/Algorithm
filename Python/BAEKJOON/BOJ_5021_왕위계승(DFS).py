import sys
sys.stdin = open('BOJ_5021.txt', 'r')

def DFS(parent ,child, last_King):
    if child == last_King:
        return 1
    if child not in parent.keys():
        return 0
    return DFS(parent, parent[child][0], last_King)/2 + DFS(parent, parent[child][1], last_King)/2

N, M = map(int, input().split())
maxBrood = 0
next_King = ''
last_King = input()
parent = {}
for _ in range(N):
    child = input().split()
    parent[child[0]] = [child[1], child[2]]
for _ in range(M):
    child = input()
    temp = DFS(parent, child, last_King)
    if temp > maxBrood:
        next_King = child
        maxBrood = temp
print(next_King)