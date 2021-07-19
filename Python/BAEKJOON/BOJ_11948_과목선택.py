import sys
sys.stdin = open('BOJ_11948.txt', 'r')

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

print(sum(sorted([A, B, C, D], reverse=True)[:3]) + max(E, F))