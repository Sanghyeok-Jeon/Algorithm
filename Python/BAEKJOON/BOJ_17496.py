import sys
sys.stdin = open('BOJ_17496.txt', 'r')

N, T, C, P = map(int, input().split())
print(C * P * ((N-1) // T))