import sys
sys.stdin = open('4299.txt', 'r')

T = int(input())

for tc in range(T):
    D, H, M = map(int, input().split())
    baseTime = 24*60*11 + 60*11 + 11
    realizeTime = 24*60*D + 60*H + M

    print('#{} {}'.format(tc+1, realizeTime-baseTime if realizeTime >= baseTime else -1))