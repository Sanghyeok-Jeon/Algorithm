import sys
sys.stdin = open('BOJ_2869.txt', 'r')

A, B, V = map(int, input().split())
print((V - B - 1) // (A - B) + 1)