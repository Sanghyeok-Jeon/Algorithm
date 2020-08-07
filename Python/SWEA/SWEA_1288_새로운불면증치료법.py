import sys
sys.stdin = open('1288.txt', 'r')

def DFS(N):
    global count, init_N
    count += 1
    temp_N = N

    while True:
        if temp_N > 9:
            num[temp_N%10] += 1
            temp_N //= 10
        else:
            num[temp_N] += 1
            break

    if 0 not in num:
        return N
    else:
        DFS(N + init_N)

T = int(input())

for tc in range(T):
    N = int(input())
    init_N = N
    num = [0] * 10
    count = 0

    DFS(N)

    result = init_N * count

    print('#{} {}'.format(tc+1, result))



