import sys
sys.stdin = open('2948.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    s_N = list(input().split())
    s_M = list(input().split())

    same_word = len(set(s_N) & set(s_M))

    print('#{} {}'.format(tc+1, same_word))
