import sys
sys.stdin = open('BOJ_4880.txt', 'r')

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    if b-a == c-b:
        print('AP {}'.format(c + (b-a)))
    else:
        print('GP {}'.format(c * (b//a)))