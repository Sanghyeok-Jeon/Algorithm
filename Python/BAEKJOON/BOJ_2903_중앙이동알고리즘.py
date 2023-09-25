import sys
sys.stdin = open('BOJ_2903.txt', 'r')

N = int(input())
print((2**N+1)**2)