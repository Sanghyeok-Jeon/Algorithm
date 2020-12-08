import sys
sys.stdin = open('BOJ_1085.txt', 'r')

x, y, w, h = map(int, input().split())
print(min(abs(x-w), abs(y-h), x, y))