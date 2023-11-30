import sys
sys.stdin = open('BOJ_16248.txt', 'r')

A, B = map(int, input().split())

q, r = A//B, A%B
if r < 0:
    q += 1
    r = A - q*B

print(q)
print(r)
