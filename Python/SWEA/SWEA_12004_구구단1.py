import sys
sys.stdin = open('SWEA_12004.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    oneToNine = list(range(1, 10))
    answer = 'No'

    for i in range(1, 10):
        if N // i in oneToNine and N % i == 0:
            answer = 'Yes'
            break

    print('#{} {}'.format(tc, answer))