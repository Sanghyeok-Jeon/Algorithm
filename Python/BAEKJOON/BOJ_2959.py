import sys
sys.stdin = open('BOJ_2959.txt', 'r')

A, B, C, D = map(int, input().split())
data = sorted([A, B, C, D])
print(data[0] * data[2])