import sys
sys.stdin = open('BOJ_5043.txt', 'r')

N, b = map(int, input().split())
print('yes' if N < (2<<b) else 'no')