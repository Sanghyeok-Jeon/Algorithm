import sys
sys.stdin = open('BOJ_2523.txt', 'r')

N = int(input())
for n in range(1, 2*N):
    if n > N:
        print('*'*(2*N-n))
    else:
        print('*'*n)