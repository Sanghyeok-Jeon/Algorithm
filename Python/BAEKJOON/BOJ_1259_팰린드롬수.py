import sys
sys.stdin = open('BOJ_1259.txt', 'r')

while True:
    num = input()

    if num == '0':
        break

    if num == num[::-1]:
        print('yes')
    else:
        print('no')