import sys
sys.stdin = open('SWEA_5604.txt', 'r')

def check(n, t):
    global sum_range
    while n > 0:
        sum_range += (n % 10) * t
        n //= 10

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    sum_range = 0

    tens = 1
    while A <= B:
        while A % 10 != 0 and A <= B:
            check(A, tens)
            A += 1

        if A > B or (A == 0 and B == 0):
            break

        while B % 10 != 9 and A <= B:
            check(B, tens)
            B -= 1

        A //= 10
        B //= 10

        cnt = (B-A+1) * tens
        for i in range(10):
            sum_range += cnt * i
        tens *= 10

    print('#{} {}'.format(tc+1, sum_range))