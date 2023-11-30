import sys
sys.stdin = open('BOJ_4388.txt', 'r')

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    cnt = 0
    prev = 0
    while a > 0 or b > 0:
        if a%10 + b%10 + prev >= 10:
            cnt += 1
            prev = 1
        else:
            prev = 0
        a //= 10
        b //= 10

    print(cnt)