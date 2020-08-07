import sys
sys.stdin = open('5431.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    student = list(map(int, input().split()))

    submit = [0] * (N+1)
    for i in range(K):
        submit[student[i]] = 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(1, N+1):
        if submit[i] == 0:
            print(i, end=' ')
    print()