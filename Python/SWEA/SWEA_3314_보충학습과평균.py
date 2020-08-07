import sys
sys.stdin = open('3314.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    sum_after_score = 0

    for i in range(5):
        if data[i] < 40:
            sum_after_score += 40
        else:
            sum_after_score += data[i]

    print('#{} {}'.format(tc+1, sum_after_score//5))