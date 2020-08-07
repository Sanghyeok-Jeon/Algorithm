import sys
sys.stdin = open('1974.txt', 'r')

def check(i, j):
    global fail_check

    temp_lst = []
    for x in range(9):
        temp_lst.append(data[i][x])
    if sorted(temp_lst) != perfect:
        fail_check += 1

    temp_lst = []
    for y in range(9):
        temp_lst.append(data[y][j])
    if sorted(temp_lst) != perfect:
        fail_check += 1

    temp_lst = []
    for x in range((i//3) * 3, (i//3) * 3 + 3):
        for y in range((j//3) * 3, (j//3) * 3 + 3):
            temp_lst.append(data[x][y])
    if sorted(temp_lst) != perfect:
        fail_check += 1

    return

T = int(input())

for tc in range(T):
    data = []
    for _ in range(9):
        data.append(list(map(int, input().split())))
    fail_check = 0
    perfect = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        for j in range(9):
            check(i, j)

    print('#{} {}'.format(tc+1, 1 if fail_check == 0 else 0))
