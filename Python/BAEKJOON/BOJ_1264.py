import sys
sys.stdin = open('BOJ_1264.txt', 'r')

vowel = 'AaEeIiOoUu'

while True:
    data = input()
    if data == '#':
        break

    cnt = 0
    for d in data:
        if d in vowel:
            cnt += 1

    print(cnt)