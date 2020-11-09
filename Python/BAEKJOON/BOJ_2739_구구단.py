import sys
sys.stdin = open('BOJ_2739.txt', 'r')

N = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(N, i, N * i))