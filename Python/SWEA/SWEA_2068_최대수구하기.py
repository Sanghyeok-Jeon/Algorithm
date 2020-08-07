import sys
sys.stdin = open('2068.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    data.sort()
    print('#{} {}'.format(tc+1, data[-1]))