import sys
sys.stdin = open('BOJ_2914.txt', 'r')

A, I = map(int, input().split())
print(A*(I-1)+1)