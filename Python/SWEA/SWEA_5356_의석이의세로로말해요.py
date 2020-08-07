import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())

for tc in range(T):
    data = []
    for _ in range(5):
        data.append(input())

    result = ''

    for j in range(15):
        for i in range(5):
            if j+1 > len(data[i]):
                continue

            result += data[i][j]

    print('#{} {}'.format(tc+1, result))