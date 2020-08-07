import sys
sys.stdin = open('10200.txt', 'r', encoding='latin_1')

T = int(input())

for tc in range(T):
    N, A, B = map(int, input().split())

    max_duplicate = A if A < B else B
    min_duplicate = 0 if A+B < N else A+B-N

    print('#{} {} {}'.format(tc+1, max_duplicate, min_duplicate))