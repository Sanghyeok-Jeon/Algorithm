import sys
sys.stdin = open('5986.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    result = 0

    prime = []
    for n in range(2, N):
        count = 0
        for z in range(2, n):
            if count == 1:
                break
            if n % z == 0:
                count = 1
        if count == 0:
            prime.append(n)

    for i in range(0, len(prime)):
        for j in range(i, len(prime)):
            if prime[i] + prime[j] >= N:
                break
            for k in range(j, len(prime)):
                if prime[i] + prime[j] + prime[k] == N:
                    result += 1

    print('#{} {}'.format(tc+1, result))

