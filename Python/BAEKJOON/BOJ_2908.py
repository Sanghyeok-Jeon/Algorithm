import sys
sys.stdin = open('BOJ_2908.txt', 'r')

A, B = input().split()
a, b = A[::-1], B[::-1]
if int(a) > int(b):
    print(a)
else:
    print(b)