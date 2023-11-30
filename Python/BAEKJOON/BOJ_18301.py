import sys
sys.stdin = open('BOJ_18301.txt', 'r')

n1, n2, n12 = map(int, input().split())
print((n1+1)*(n2+1)//(n12+1)-1)