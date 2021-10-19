import sys
sys.stdin = open('BOJ_1673.txt', 'r')

for tc in sys.stdin.readlines():
    n, k = map(int, tc.strip().split())
    chicken = n
    while n // k:
        chicken += n // k
        n = n//k + n%k
    print(chicken)
