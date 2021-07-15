import sys
sys.stdin = open('BOJ_3004.txt', 'r')

N = int(input())
r = N // 2
c = N - r
print((r+1) * (c+1))