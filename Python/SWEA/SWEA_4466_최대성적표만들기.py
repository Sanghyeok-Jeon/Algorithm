import sys
sys.stdin = open('4466.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i, N):
            if scores[i] < scores[j]:
                scores[i], scores[j] = scores[j], scores[i]

    max_sum = 0
    for i in range(K):
        max_sum += scores[i]

    print('#{} {}'.format(tc+1, max_sum))