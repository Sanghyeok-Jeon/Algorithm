import sys
sys.stdin = open('BOJ_15963.txt', 'r')

N, M = map(int, input().split())
print(1 if N == M else 0)