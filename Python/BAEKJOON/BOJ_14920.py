import sys
sys.stdin = open('BOJ_14920.txt', 'r')

for _ in range(2):
    num = int(input())

    idx = 1
    while True:
        if num == 1:
            break

        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num = num // 2

        idx += 1

    print(idx)