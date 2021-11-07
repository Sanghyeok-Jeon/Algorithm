import sys
sys.stdin = open('SWEA_11856.txt', 'r')

T = int(input())
for tc in range(T):
    data = input()
    cntAlpha = {}
    answer = 'No'

    for i in range(4):
        if data[i] in cntAlpha:
            cntAlpha[data[i]] += 1
        else:
            cntAlpha[data[i]] = 1

    if len(cntAlpha) == 2 and cntAlpha[data[0]] == 2:
        answer = 'Yes'

    print('#{} {}'.format(tc+1, answer))