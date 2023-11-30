import sys
sys.stdin = open('BOJ_15700.txt', 'r')

N, M = map(int, input().split())
print(N*M//2)