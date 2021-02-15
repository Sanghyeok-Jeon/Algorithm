import sys
sys.stdin = open('SWEA_1223.txt', 'r')

for tc in range(1, 11):
    length = int(input())
    data = input()
    ans = 0
    stackNumber = []

    checkMultiple = 0
    for i in range(length):
        if not i % 2:
            stackNumber.append(int(data[i]))
            if checkMultiple:
                stackNumber.append(stackNumber.pop() * stackNumber.pop())
                checkMultiple = 0
        else:
            if data[i] == '*':
                checkMultiple = 1

    ans = sum(stackNumber)

    print('#{} {}'.format(tc, ans))