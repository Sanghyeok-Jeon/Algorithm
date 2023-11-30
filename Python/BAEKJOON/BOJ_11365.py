import sys
sys.stdin = open('BOJ_11365.txt', 'r')

while True:
    data = input()
    if data == 'END':
        break

    print(data[::-1])