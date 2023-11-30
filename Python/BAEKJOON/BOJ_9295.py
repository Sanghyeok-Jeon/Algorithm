import sys
sys.stdin = open('BOJ_9295.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    print('Case {}: {}'.format(tc, a+b))