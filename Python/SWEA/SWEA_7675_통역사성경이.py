import sys
sys.stdin = open('7675.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(input().split())
    result = [0] * N
    sentenceNum = 0

    r = 0
    i = 0
    for i in range(len(data)):
        if len(data[i]) == 1:
            if ord('A') <= ord(data[i]) <= ord('Z'):
                result[r] += 1
            elif data[i] in ('.', '?', '!'):
                r += 1
        else:
            fail = 0
            for j in range(len(data[i])):
                if j == len(data[i]) - 1:
                    if data[i][j] in ('.', '?', '!'):
                        if fail == 0:
                            result[r] += 1
                        r += 1
                    elif fail == 0 and ord('a') <= ord(data[i][j]) <= ord('z'):
                        result[r] += 1
                    break

                if j == 0:
                    if ord(data[i][j]) < ord('A') or ord(data[i][j]) > ord('Z'):
                        fail = 1
                else:
                    if ord('a') <= ord(data[i][j]) <= ord('z'):
                        pass
                    else:
                        fail = 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(N):
        print('{}'.format(result[i]), end=' ')
    print()