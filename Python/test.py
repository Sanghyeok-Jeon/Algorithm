import sys
sys.stdin = open('SWEA/SWEA_7701.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = [input() for _ in range(N)]
    result = list(set(data))
    result.sort()

    print('#{}'.format(tc+1))
    for i in range(len(result)):
        print(result[i])