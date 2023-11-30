import sys
sys.stdin = open('BOJ_2439.txt', 'r')

N = int(input())
for i in range(N):
    print(' ' * (N-(i+1)), end='')
    print('*' * (i+1))