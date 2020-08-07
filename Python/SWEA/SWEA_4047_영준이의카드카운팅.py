import sys
sys.stdin = open('4047.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()
    S_visited = [0] * 14
    D_visited = [0] * 14
    H_visited = [0] * 14
    C_visited = [0] * 14
    error = 0

    for i in range(0, len(data), 3):
        n = int(data[i+1:i+3])
        if data[i] == 'S':
            if S_visited[n]:
                error = 1
                break
            else:
                S_visited[n] = 1
                S_visited[0] += 1
        elif data[i] == 'D':
            if D_visited[n]:
                error = 1
                break
            else:
                D_visited[n] = 1
                D_visited[0] += 1
        elif data[i] == 'H':
            if H_visited[n]:
                error = 1
                break
            else:
                H_visited[n] = 1
                H_visited[0] += 1
        else:
            if C_visited[n]:
                error = 1
                break
            else:
                C_visited[n] = 1
                C_visited[0] += 1

    if error:
        print('#{} {}'.format(tc+1, 'ERROR'))
    else:
        print('#{} {} {} {} {}'.format(tc+1, 13-S_visited[0], 13-D_visited[0], 13-H_visited[0], 13-C_visited[0]))
