import sys
sys.stdin = open('SWEA_10570.txt', 'r')

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        if i**0.5 % 1 == 0:
            if str(i) == str(i)[::-1] and str(int(i**0.5)) == str(int(i**0.5))[::-1]:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))