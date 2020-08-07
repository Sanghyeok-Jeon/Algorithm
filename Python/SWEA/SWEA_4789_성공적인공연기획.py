import sys
sys.stdin = open('4789.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input()))
    need_people = 0

    temp_sum = 0
    for i in range(len(data)):
        if i > temp_sum:
            need_people += i - temp_sum
            temp_sum = i + data[i]
        else:
            temp_sum += data[i]

    print('#{} {}'.format(tc+1, need_people))
