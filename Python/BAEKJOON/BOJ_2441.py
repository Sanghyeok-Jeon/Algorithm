import sys
sys.stdin = open('BOJ_2441.txt', 'r')

N = int(input())
for n in range(N):
    print(' '*n + '*'*(N-n))