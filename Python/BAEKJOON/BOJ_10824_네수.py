import sys
sys.stdin = open('BOJ_10824.txt', 'r')

A, B, C, D = input().split()
print(int(A+B) + int(C+D))