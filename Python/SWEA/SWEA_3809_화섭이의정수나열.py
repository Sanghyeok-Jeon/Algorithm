import sys
sys.stdin = open('3809.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = []
    while len(data) != N:
        data += list(input().split())
    result = -1

    num = []
    len_str = 1
    while len_str <= N:
        for i in range(0, N-len_str+1):
            number = int(''.join(data[i:i+len_str]))
            if number not in num:
                num.append(number)

        for i in range(0, max(num)):
            if i not in num:
                result = i
                break

        if result != -1:
            break

        len_str += 1

    print('#{} {}'.format(tc+1, result))