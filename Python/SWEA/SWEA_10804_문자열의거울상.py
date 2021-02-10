import sys
sys.stdin = open('SWEA_10804.txt', 'r')

T = int(input())
for tc in range(T):
    strInput = input()
    mirror = []
    for s in strInput:
        if s == 'b':
            mirror.append('d')
        elif s == 'd':
            mirror.append('b')
        elif s == 'p':
            mirror.append('q')
        else:
            mirror.append('p')
    print('#{} {}'.format(tc+1, ''.join(mirror[::-1])))