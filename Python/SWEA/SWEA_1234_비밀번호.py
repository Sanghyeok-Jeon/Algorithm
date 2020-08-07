import sys
sys.stdin = open('1234.txt', 'r')

T = 10

for tc in range(T):
    n, d = input().split()
    data = list(d)
    N = len(data)
    stack = []

    i = 0
    while True:
        if i == N:
            break

        if len(stack):
            if data[i] != stack[-1]:
                stack.append(data[i])
            else:
                stack.pop()
        else:
            stack.append(data[i])

        i += 1

    print('#{} {}'.format(tc+1, ''.join(stack)))