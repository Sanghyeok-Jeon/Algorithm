import sys
sys.stdin = open('BOJ_8393.txt', 'r')

n = int(input())
print(n * (n+1) // 2)