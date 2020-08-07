import sys
sys.stdin = open('4579.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()

    fail = 0
    for i in range(len(data)//2):
        if data[i] == '*' or data[-1-i] == '*':
            fail = 0
            break
        if data[i] != data[-1-i]:
            fail = 1
            break

    print('#{} {}'.format(tc+1, 'Not exist' if fail else 'Exist'))