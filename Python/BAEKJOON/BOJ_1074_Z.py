import sys
sys.stdin = open('BOJ_1074.txt', 'r')

def divide(length, start_r, start_c):
    global cnt, r, c
    if length == 2:
        if start_r == r and start_c == c:
            print(cnt)
            return
        cnt += 1
        if start_r == r and start_c+1 == c:
            print(cnt)
            return
        cnt += 1
        if start_r+1 == r and start_c == c:
            print(cnt)
            return
        cnt += 1
        if start_r+1 == r and start_c+1 == c:
            print(cnt)
            return
        cnt += 1
    else:
        divide(length//2, start_r, start_c)
        divide(length//2, start_r, start_c + length//2)
        divide(length//2, start_r + length//2, start_c)
        divide(length//2, start_r + length//2, start_c + length//2)

T = int(input())

for tc in range(T):
    N, r, c = map(int, input().split())
    cnt = 0

    divide(2**N, 0, 0)