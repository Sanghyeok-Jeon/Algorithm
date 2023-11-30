import sys
sys.stdin = open('BOJ_8370.txt', 'r')

n1, k1, n2, k2 = map(int, input().split())
print(n1*k1 + n2*k2)