import sys
sys.stdin = open('BOJ_2338.txt', 'r')

A, B = int(input()), int(input())
print(A+B, A-B, A*B, sep='\n')