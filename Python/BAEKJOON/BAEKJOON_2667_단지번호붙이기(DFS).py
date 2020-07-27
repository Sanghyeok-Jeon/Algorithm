import sys
sys.stdin = open('BAEKJOON_2667.txt', 'r')

def DFS(i, j):
    global temp_group

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N and 0 <= nj < N and APT[ni][nj]:
            APT[ni][nj] = 0
            temp_group += 1
            DFS(ni, nj)

N = int(input())
APT = [list(map(int, input())) for _ in range(N)]
group_num = []

for i in range(N):
    for j in range(N):
        if APT[i][j]:
            temp_group = 1
            APT[i][j] = 0
            DFS(i, j)
            group_num.append(temp_group)

for i in range(len(group_num)-1):
    for j in range(i+1, len(group_num)):
        if group_num[i] > group_num[j]:
            group_num[i], group_num[j] = group_num[j], group_num[i]


print(len(group_num))
for i in range(len(group_num)):
    print(group_num[i])