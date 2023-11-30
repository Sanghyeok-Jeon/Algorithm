import sys
sys.stdin = open('BOJ_15964.txt', 'r')

A, B = map(int, input().split())
print((A+B)*(A-B))