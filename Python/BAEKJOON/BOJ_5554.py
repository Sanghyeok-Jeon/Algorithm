import sys
sys.stdin = open('BOJ_5554.txt', 'r')

time = sum(map(int, sys.stdin))
print(time//60)
print(time%60)