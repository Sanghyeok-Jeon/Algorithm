import sys
sys.stdin = open('1215.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    data = [input() for _ in range(8)]
    count_pal = 0

    for i in range(8):
        for j in range(8-N+1):
            temp_char = ''
            for k in range(N):
                temp_char += data[i][j+k]
            if temp_char == temp_char[::-1]:
                count_pal += 1

    for j in range(8):
        for i in range(8-N+1):
            temp_char = ''
            for k in range(N):
                temp_char += data[i+k][j]
            if temp_char == temp_char[::-1]:
                count_pal += 1

    print('#{} {}'.format(tc+1, count_pal))