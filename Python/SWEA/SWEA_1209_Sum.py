import sys
sys.stdin = open('1209.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for i in range(100):
        sum_i = 0
        sum_j = 0
        for j in range(100):
            sum_i += data[i][j]
            sum_j += data[j][i]
        if sum_i > max_sum:
            max_sum = sum_i
        if sum_j > max_sum:
            max_sum = sum_j

    for i in range(100):
        sum_LR = 0
        sum_RL = 0
        for j in range(100):
            sum_LR += data[i][j]
            sum_RL += data[i][100-j-1]
        if sum_LR > max_sum:
            max_sum = sum_LR
        if sum_RL > max_sum:
            max_sum = sum_RL

    print('#{} {}'.format(tc+1, max_sum))


