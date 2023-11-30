import sys
sys.stdin = open('BOJ_10991.txt', 'r')

N = int(input())
for n in range(1, N+1):
    print(' '*(N-n) + '* '*n)