import sys
sys.stdin = open('BOJ_15726.txt', 'r')

A, B, C = map(int, input().split())
print(int(max(A*B/C, A/B*C)))