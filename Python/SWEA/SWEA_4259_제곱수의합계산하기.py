import sys
sys.stdin = open('SWEA_4259.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())
    data = list(input().split())

    answer = 0
    for i in range(n):
        answer += int(data[i][0:len(data[i])-1]) ** int(data[i][-1])

    print('#{} {}'.format(tc+1, answer))