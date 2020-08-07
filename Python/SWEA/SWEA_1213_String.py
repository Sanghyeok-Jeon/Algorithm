import sys
sys.stdin = open('1213.txt', 'r', encoding='latin_1')

T = 10

for tc in range(T):
    N = int(input())
    target = input()
    length_target = len(target)
    data = input()
    count_target = 0

    for i in range(len(data)):
        if data[i] == target[0]:
            if data[i:i+length_target] == target:
                count_target += 1

    print('#{} {}'.format(tc+1, count_target))