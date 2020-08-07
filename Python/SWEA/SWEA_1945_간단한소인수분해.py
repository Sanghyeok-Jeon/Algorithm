import sys
sys.stdin = open('1945.txt', 'r')

T = int(input())

for tc in range(T):
    num = int(input())
    a = b = c = d = e = 0

    while True:
        if num % 2 != 0:
            break
        else:
            num //= 2
            a += 1

    while True:
        if num % 3 != 0:
            break
        else:
            num //= 3
            b += 1

    while True:
        if num % 5 != 0:
            break
        else:
            num //= 5
            c += 1

    while True:
        if num % 7 != 0:
            break
        else:
            num //= 7
            d += 1

    while True:
        if num % 11 != 0:
            break
        else:
            num //= 11
            e += 1

    print('#{} {} {} {} {} {}'.format(tc+1, a, b, c, d, e))

