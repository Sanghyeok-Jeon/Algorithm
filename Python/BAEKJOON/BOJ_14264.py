import sys
sys.stdin = open('BOJ_14264.txt', 'r')

L = int(input())
print(round((L/2)*(L/2)*(3**0.5), 9))