import sys
sys.stdin = open('SWEA_1222.txt', 'r')

for tc in range(10):
    len_data = int(input())
    data = input()

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = 0
    for i in range(len(data)):
        if data[i] in numbers:
            answer += int(data[i])

    print('#{} {}'.format(tc+1, answer))