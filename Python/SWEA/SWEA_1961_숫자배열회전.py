import sys
sys.stdin = open('1961.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*3 for _ in range(N)]

    for j in range(N):
        temp_str = ''
        for i in range(N-1, -1, -1):
            temp_str += str(data[i][j])
        result[j][0] = temp_str

    for i in range(N-1, -1, -1):
        temp_str = ''
        for j in range(N-1, -1, -1):
            temp_str += str(data[i][j])
        result[N-1-i][1] = temp_str

    for j in range(N-1, -1 ,-1):
        temp_str = ''
        for i in range(N):
            temp_str += str(data[i][j])
        result[N-1-j][2] = temp_str

    print('#{}'.format(tc+1))
    for i in range(N):
        for j in range(3):
            print(result[i][j], end=' ')
        print()