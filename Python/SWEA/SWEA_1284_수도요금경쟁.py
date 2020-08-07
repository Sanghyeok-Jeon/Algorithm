import sys
sys.stdin = open('1284.txt', 'r')

T = int(input())

for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    cost_P = P * W
    cost_Q = Q if W < R else Q + S * (W - R)

    print('#{} {}'.format(tc+1, cost_P if cost_P < cost_Q else cost_Q))