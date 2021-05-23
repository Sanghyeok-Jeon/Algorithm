import sys
sys.stdin = open('BOJ_4458.txt', 'r')

N = int(input())
for _ in range(N):
    data = list(input())
    data[0] = data[0].upper()
    print(''.join(data))