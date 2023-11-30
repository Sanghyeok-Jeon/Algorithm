import sys
sys.stdin = open('BOJ_5717.txt', 'r')

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    print(a+b)