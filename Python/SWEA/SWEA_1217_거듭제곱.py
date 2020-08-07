import sys
sys.stdin = open('1217.txt', 'r')

def multi_power(m):
    global N, M, result

    if m == M:
        return
    else:
        result *= N
        multi_power(m+1)

T = 10

for tc in range(T):
    testcase = int(input())
    N, M = map(int, input().split())

    result = 1
    multi_power(0)

    print('#{} {}'.format(tc+1, result))