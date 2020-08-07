import sys
sys.stdin = open('1946.txt', 'r')

T = int(input())

for tc in range(T):
    data = ''
    N = int(input())
    for _ in range(N):
        chr, num = map(str, input().split())
        data += chr * int(num)

    print('#{}'.format(tc+1))
    for i in range(0, len(data), 10):
        print(data[i:i+10])