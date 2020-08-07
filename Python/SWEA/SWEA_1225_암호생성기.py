import sys
sys.stdin = open('1225.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    minus = 1
    while True:
        if data[0] <= minus:
            change_data = 0
            data = data[1:]
            data.append(change_data)
            break

        change_data = data[0] - minus
        data = data[1:]
        data.append(change_data)

        if minus < 5:
            minus += 1
        else:
            minus = 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(8):
        print(data[i], end=' ')
    print()