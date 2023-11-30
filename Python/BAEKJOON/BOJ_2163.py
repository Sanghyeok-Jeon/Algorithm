import sys
sys.stdin = open('BOJ_2163.txt', 'r')

N, M = map(int, input().split())
print((N-1) + (M-1)*N)