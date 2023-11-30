import sys
sys.stdin = open('BOJ_2442.txt', 'r')

N = int(input())
for i in range(N):
    print(' '*(N-1-i) + '*'*(2*i+1))