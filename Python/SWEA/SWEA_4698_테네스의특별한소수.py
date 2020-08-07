import sys
sys.stdin = open('4698.txt', 'r')

n = 1000000
a = [0, 0] + [1] * (n-1)
prime = []
for i in range(2, n+1):
    if a[i]:
        prime.append(i)
        for j in range(i*2, n+1, i):
            a[j] = 0

T = int(input())

for tc in range(T):
    D, A, B = map(int, input().split())

    result = 0
    for i in range(len(prime)):
        if A <= prime[i] <= B:
            if str(D) in str(prime[i]):
                result += 1

    print('#{} {}'.format(tc+1, result))
