import sys
sys.stdin = open('BOJ_2522.txt', 'r')

N = int(input())
for n in range(1, 2*N):
    print(' '*abs(N-n) + '*'*(N-abs(N-n)))