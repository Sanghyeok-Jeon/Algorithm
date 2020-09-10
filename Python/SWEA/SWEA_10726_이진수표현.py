import sys
sys.stdin = open('SWEA_10726.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    data = format(M, 'b')

    possible = 0
    if data[::-1][:N] == '1' * N:
        possible = 1

    print('#{} {}'.format(tc+1, 'ON' if possible else 'OFF'))