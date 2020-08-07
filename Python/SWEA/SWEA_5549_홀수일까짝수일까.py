import sys
sys.stdin = open('5549.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    print('#{} {}'.format(tc+1, 'Odd' if N % 2 else 'Even'))