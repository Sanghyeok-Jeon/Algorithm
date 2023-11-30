import sys
sys.stdin = open('BOJ_16204.txt', 'r')

N, M, K = map(int, input().split())

if K > M:
    print(N - (K-M))
elif K < M:
    print(N - (M-K))
else:
    print(N)