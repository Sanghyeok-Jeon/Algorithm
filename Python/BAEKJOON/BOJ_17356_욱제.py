import sys
sys.stdin = open('BOJ_17356.txt', 'r')

A, B = map(int, input().split())
M = (B-A) / 400
ukje = 1 / (1+10**M)
print(ukje)