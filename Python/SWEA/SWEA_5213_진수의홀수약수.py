import sys
sys.stdin = open('SWEA_5213.txt', 'r')

sum_yaksu = [0] * 1000001
for i in range(1, 1000001, 2):
    for j in range(i, 1000001, i):
        sum_yaksu[j] += i

for i in range(1000000):
    sum_yaksu[i+1] += sum_yaksu[i]

T = int(input())

answer = []
for tc in range(T):
    L, R = map(int, input().split())
    answer.append('#' + str(tc+1) + ' ' + str(sum_yaksu[R] - sum_yaksu[L-1]))

print(*answer, sep='\n')