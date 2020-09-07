import sys
sys.stdin = open('SWEA_2819.txt', 'r')

def DFS(i, j, cnt, tmp):
    if cnt == 7:
        if tmp not in numbers:
            numbers.add(tmp)
        return

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(ni, nj, cnt+1, tmp+data[ni][nj])

T = int(input())

for tc in range(T):
    data = [list(input().split()) for _ in range(4)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    numbers = set()
    for i in range(4):
        for j in range(4):
            DFS(i, j, 1, data[i][j])

    print('#{} {}'.format(tc+1, len(numbers)))