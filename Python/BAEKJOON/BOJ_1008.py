import sys
sys.stdin = open('BOJ_1008.txt', 'r')

A, B = map(int, input().split())
print('{0:0.9f}'.format(A/B))