import sys
sys.stdin = open('1959.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst_N = list(map(int, input().split()))
    lst_M = list(map(int, input().split()))
    total = 0

    if N <= M:
        for i in range(M-N+1):
            temp_total = 0
            for j in range(N):
                temp_total += lst_N[j] * lst_M[i+j]
            if temp_total > total:
                total = temp_total
    else:
        for i in range(N-M+1):
            temp_total = 0
            for j in range(M):
                temp_total += lst_M[j] * lst_N[i+j]
            if temp_total > total:
                total = temp_total

    print('#{} {}'.format(tc+1, total))
