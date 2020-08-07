import sys
sys.stdin = open('6019.txt', 'r')

T = int(input())

for tc in range(T):
    D, A, B, F = map(int, input().split())

    print('#{} {}'.format(tc+1, D/(A+B) * F))