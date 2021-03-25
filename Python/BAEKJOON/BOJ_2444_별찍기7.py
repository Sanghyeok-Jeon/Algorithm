import sys
sys.stdin = open('BOJ_2444.txt', 'r')

N = int(input())
for i in range(1, N*2):
    print(' '*abs(N-i) + '*'*((N-abs(N-i))*2-1))