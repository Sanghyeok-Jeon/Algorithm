import sys
sys.stdin = open('BOJ_14924.txt', 'r')

S, T, D = map(int, input().split())
F = D // (S*2) * T
print(F)