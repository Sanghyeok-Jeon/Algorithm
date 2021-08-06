import sys
sys.stdin = open('BOJ_2355.txt', 'r')

A, B = map(int, input().split())
if A > B:
    A, B = B, A
print((B - A + 1) * (A + B) // 2)