import sys
sys.stdin = open('SWEA_10912.txt', 'r')

T = int(input())
for tc in range(T):
    strInput = input()
    dic = {}
    for s in strInput:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    result = []
    for key, value in dic.items():
        if value % 2:
            result.append(key)

    if len(result):
        print('#{} {}'.format(tc+1, ''.join(sorted(result))))
    else:
        print('#{} {}'.format(tc+1, "Good"))