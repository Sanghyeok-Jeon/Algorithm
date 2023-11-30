import sys
sys.stdin = open('BOJ_1271.txt', 'r')

n, m = map(int, input().split())
print(n // m)
print(n % m)