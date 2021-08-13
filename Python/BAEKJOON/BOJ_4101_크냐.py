import sys
sys.stdin = open('BOJ_4101.txt', 'r')

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    print('Yes' if A > B else 'No')