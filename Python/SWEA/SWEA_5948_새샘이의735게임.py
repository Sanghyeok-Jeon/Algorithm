import sys
sys.stdin = open('5948.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    sum_3data = []

    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                sum_temp = data[i] + data[j] + data[k]
                if sum_temp not in sum_3data:
                    sum_3data.append(sum_temp)

    for i in range(len(sum_3data)-1):
        for j in range(i, len(sum_3data)):
            if sum_3data[i] > sum_3data[j]:
                sum_3data[i], sum_3data[j] = sum_3data[j], sum_3data[i]

    print('#{} {}'.format(tc+1, sum_3data[-5]))