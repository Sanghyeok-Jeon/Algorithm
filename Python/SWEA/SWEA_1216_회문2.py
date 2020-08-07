import sys
sys.stdin = open('1216.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    data = [input() for _ in range(100)]
    n = len(data)
    max_len_pal = -1

    len_char = 100
    while len_char > 0:
        find = 0
        for i in range(n):
            for j in range(n-len_char+1):
                success = True
                for k in range(len_char//2):
                    if data[i][j+k] != data[i][j+len_char-k-1]:
                        success = False
                        break
                if success:
                    max_len_pal = len_char
                    find = 1
                    break
            if find:
                break
        if find:
            break

        find = 0
        for j in range(n):
            for i in range(n - len_char + 1):
                success = True
                for k in range(len_char // 2):
                    if data[i+k][j] != data[i + len_char - k - 1][j]:
                        success = False
                        break
                if success:
                    max_len_pal = len_char
                    find = 1
                    break
            if find:
                break
        if find:
            break

        len_char -= 1

    print('#{} {}'.format(tc+1, max_len_pal))