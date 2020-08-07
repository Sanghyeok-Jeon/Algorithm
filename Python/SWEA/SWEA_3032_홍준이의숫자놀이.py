import sys
sys.stdin = open('3032.txt', 'r')

def extended_euclid(a, b):
    x, y = 0, 1
    u, v = 1, 0

    while a:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a = a, r
        x, y = u, v
        u, v = m, n

    return (x, y)

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    x, y = extended_euclid(A, B)

    print('#{} {} {}'.format(tc+1, x, y))