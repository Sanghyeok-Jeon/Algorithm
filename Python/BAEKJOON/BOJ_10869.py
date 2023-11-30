import sys
sys.stdin = open('BOJ_10869.txt', 'r')

A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)