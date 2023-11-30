import sys
sys.stdin = open('BOJ_10988.txt', 'r')

data = input()
print(1 if data == data[::-1] else 0)