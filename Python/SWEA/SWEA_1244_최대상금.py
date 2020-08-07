import sys
sys.stdin = open('1244.txt', 'r')

def DFS(number, cnt_change):
    global num, max_num, cnt
    temp_num = int(''.join(number))

    if cnt_change == 0:
        if temp_num > max_num:
            max_num = temp_num
        return

    if visited[cnt_change] > temp_num:
        return
    visited[cnt_change] = temp_num

    for i in range(0, len(number)-1):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            DFS(number, cnt_change-1)
            number[i], number[j] = number[j], number[i]

T = int(input())

for tc in range(T):
    data, cnt = map(int, input().split())
    num = list(str(data))
    max_num = 0
    visited = [0] * (cnt+1)

    DFS(num, cnt)

    print('#{} {}'.format(tc+1, max_num))