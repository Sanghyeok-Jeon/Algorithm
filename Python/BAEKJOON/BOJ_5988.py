import sys
sys.stdin = open('BOJ_5988.txt', 'r')

N = int(input())
for _ in range(N):
    print('odd' if int(input())%2 else 'even')