import sys
sys.stdin = open('BOJ_5893.txt', 'r')

n = input()
N = int(n, 2)
print(format(N*17, 'b'))