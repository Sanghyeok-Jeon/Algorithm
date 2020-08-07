import sys
sys.stdin = open('4406.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()
    moem = ['a', 'e', 'i', 'o', 'u']

    print('#{}'.format(tc+1), end=' ')
    for c in data:
        if c not in moem:
            print(c, end='')
    print()
