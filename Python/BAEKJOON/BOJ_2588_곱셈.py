import sys
sys.stdin = open('BOJ_2588.txt', 'r')

A = int(input())
B = input()

print(A * int(B[2]))
print(A * int(B[1]))
print(A * int(B[0]))
print(A * int(B))