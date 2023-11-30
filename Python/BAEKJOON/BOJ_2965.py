import sys
sys.stdin = open('BOJ_2965.txt', 'r')

A, B, C = map(int, input().split())
print(B-A-1 if B-A > C-B else C-B-1)