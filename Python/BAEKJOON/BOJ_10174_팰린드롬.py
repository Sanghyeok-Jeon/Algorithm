import sys
sys.stdin = open('BOJ_10174.txt', 'r')

N = int(input())
for _ in range(N):
    S = input().lower()
    if S == S[::-1]:
        print('Yes')
    else:
        print('No')