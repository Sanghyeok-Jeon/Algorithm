import sys
sys.stdin = open('SWEA_3752.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [1] + [0] * sum(score)

    cnt = []
    cnt.append(0)
    for i in range(N):
        for j in range(len(cnt)):
            if not visited[cnt[j]+score[i]]:
                visited[cnt[j] + score[i]] = 1
                cnt.append(cnt[j]+score[i])

    print('#{} {}'.format(tc+1, len(cnt)))