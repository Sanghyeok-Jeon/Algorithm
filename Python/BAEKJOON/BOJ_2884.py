import sys
sys.stdin = open('BOJ_2884.txt', 'r')

H, M = map(int, input().split())

if M >= 45:
    print('{} {}'.format(H, M-45))
else:
    if H == 0:
        print('{} {}'.format(23, 60-45+M))
    else:
        print('{} {}'.format(H-1, 60-45+M))