import sys
sys.stdin = open('BOJ_2420.txt', 'r')

N, M = map(int, input().split())
print(abs(N-M))