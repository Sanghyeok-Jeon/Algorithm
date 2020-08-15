import sys
sys.stdin = open('BOJ_2210.txt', 'r')

#1
def backtracking(i, j, tmp):
    if len(tmp) == 6:
        numbers.add(tmp)
        return

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < 5 and 0 <= nj < 5:
            backtracking(ni, nj, tmp+data[ni][nj])

data = [list(sys.stdin.readline().split()) for _ in range(5)]
numbers = set()

for i in range(5):
    for j in range(5):
        backtracking(i, j, data[i][j])

print(len(numbers))


#2
def backtracking(i, j, tmp):
    global cnt
    if len(tmp) == 6:
        if tmp not in numbers:
            numbers.append(tmp)
        return

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < 5 and 0 <= nj < 5:
            backtracking(ni, nj, tmp+data[ni][nj])

data = [list(sys.stdin.readline().split()) for _ in range(5)]
numbers = []

for i in range(5):
    for j in range(5):
        cnt = 0
        backtracking(i, j, data[i][j])

print(len(numbers))


#3
def backtracking(i, j, tmp):
    global cnt
    if i >= 5 or i < 0 or j >= 5 or j < 0:
        return

    if len(tmp) == 6:
        if tmp not in numbers:
            numbers.append(tmp)
        return

    backtracking(i+1, j, tmp+data[i][j])
    backtracking(i-1, j, tmp+data[i][j])
    backtracking(i, j+1, tmp+data[i][j])
    backtracking(i, j-1, tmp+data[i][j])

data = [list(sys.stdin.readline().split()) for _ in range(5)]
numbers = []

for i in range(5):
    for j in range(5):
        tmp = ''
        backtracking(i, j, tmp)

print(len(numbers))