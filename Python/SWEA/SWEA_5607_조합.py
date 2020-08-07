## 다시 도전 필요
import sys
sys.stdin = open('5607.txt', 'r')

def fermat(n, x):
    if x == 0:
        return 1

    temp = fermat(n, x//2)
    ret = (temp * temp) % MOD

    if x % 2 == 0:
        return ret
    else:
        return (ret * n) % MOD

T = int(input())
MOD = 1234567891

for tc in range(T):
    N, R = map(int, input().split())

    factorial = [1] * (N+1)
    for i in range(1, N+1):
        factorial[i] = factorial[i-1]*i % MOD

    bottom = (factorial[R] * factorial[N-R]) % MOD
    reBottom = fermat(bottom, MOD-2)

    print('#{} {}'.format(tc+1, (factorial[N] * reBottom) % MOD))

