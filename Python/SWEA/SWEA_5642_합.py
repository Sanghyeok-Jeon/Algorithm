import sys
sys.stdin = open('5642.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    max_sum = -(1000 * N)
    temp_sum = 0
    for i in range(N):
        temp_sum += data[i]
        if temp_sum > max_sum:
            max_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0

    print('#{} {}'.format(tc+1, max_sum))