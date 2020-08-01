import sys
sys.stdin = open('test.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    
    print(data)