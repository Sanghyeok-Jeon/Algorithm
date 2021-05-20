import sys
sys.stdin = open('BOJ_13235.txt', 'r')

S = input()
print('true' if S == S[::-1] else 'false')