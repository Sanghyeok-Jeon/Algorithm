import sys
sys.stdin = open('2019.txt', 'r')

N = int(input())

for n in range(N+1):
    print(2**n, end=' ')