import sys
sys.stdin = open('3431.txt', 'r')

T = int(input())

for tc in range(T):
    L, U, X = map(int, input().split())

    if X < L:
        more_time = L - X
    elif L <= X <= U:
        more_time = 0
    else:
        more_time = -1

    print('#{} {}'.format(tc+1, more_time))