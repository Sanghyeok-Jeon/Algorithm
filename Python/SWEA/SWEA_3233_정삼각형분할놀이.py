import sys
sys.stdin = open('3233.txt', 'r')

T = int(input())
result = []

for tc in range(T):
    A, B = map(int, input().split())
    result.append((A // B) ** 2)

x = 1
for i in range(len(result)):
    print('#{} {}'.format(x, result[i]))
    x += 1