import sys
sys.stdin = open('BOJ_15734.txt', 'r')

L, R, A = map(int, input().split())

while A:
    if L > R:
        R += 1
    else:
        L += 1
    A -= 1

print(L + R - abs(L-R))