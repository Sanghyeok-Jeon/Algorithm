import sys
sys.stdin = open('BOJ_2440.txt', 'r')

N = int(input())
for n in range(N, 0, -1):
    print('*'*n)