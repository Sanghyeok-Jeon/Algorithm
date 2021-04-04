import sys
sys.stdin = open('BOJ_10156.txt', 'r')

K, N, M = map(int, input().split())
print(K*N-M if K*N-M > 0 else 0)