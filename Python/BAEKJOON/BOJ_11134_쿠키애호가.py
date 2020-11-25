import sys
sys.stdin = open('BOJ_11134.txt', 'r')

T = int(input())
for tc in range(T):
    N, C = map(int, input().split())
    print(N // C + 1 if N % C else N // C)