import sys
sys.stdin = open('BOJ_2443.txt', 'r')

N = int(input())
for i in range(N):
    print(' '*i, end='')
    print('*'*(2*N-1-2*i))