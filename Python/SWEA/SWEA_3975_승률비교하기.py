import sys
sys.stdin = open('3975.txt', 'r')

T = int(input())
result = []

for tc in range(T):
    data = list(map(int, input().split()))
    ALICE = data[0] * data[3]
    BOB = data[1] * data[2]
    if ALICE > BOB:
        result.append('ALICE')
    else:
        if ALICE < BOB:
            result.append('BOB')
        else:
            result.append('DRAW')
tc = 1
for i in result:
    print('#{} {}'.format(tc, i))
    tc += 1