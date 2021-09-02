import sys
sys.stdin = open('BOJ_2935.txt', 'r')

A = int(input())
op = input()
B = int(input())
print(A+B if op == '+' else A*B)