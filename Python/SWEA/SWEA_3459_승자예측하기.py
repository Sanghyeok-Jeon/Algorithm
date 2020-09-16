import sys
sys.stdin = open('SWEA_3459.txt', 'r')

T = int(input())

result = []
for tc in range(T):
    N = int(input())
    x = 1

    w = False
    multiple = 1
    while x < N:
        if not w:
            multiple *= 4
        x += multiple
        w = not w

    result.append('#{} {}'.format(tc+1, 'Alice' if w else 'Bob'))
print(*result, sep='\n')