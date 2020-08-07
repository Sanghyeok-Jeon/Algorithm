import sys
sys.stdin = open('2043.txt', 'r')

a, b = map(int, input().split())

print(abs(a-b)+1)