import sys
sys.stdin = open('BOJ_11282.txt', 'r')

N = int(input())
print(chr(ord('가')+N-1))