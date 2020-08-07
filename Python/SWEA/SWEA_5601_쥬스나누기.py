import sys
sys.stdin = open('5601.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    print('#{}'.format(tc+1), end=' ')
    for _ in range(N):
        print('1/{}'.format(N), end=' ')
    print()