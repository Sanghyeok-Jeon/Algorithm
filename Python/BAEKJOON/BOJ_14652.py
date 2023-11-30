import sys
sys.stdin = open('BOJ_14652.txt', 'r')

N, M, K = map(int, input().split())
print(K//M, K%M)