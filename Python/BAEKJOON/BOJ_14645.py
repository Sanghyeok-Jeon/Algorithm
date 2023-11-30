import sys
sys.stdin = open('BOJ_14645.txt', 'r')

N, K = map(int, input().split())
for i in range(N):
    A, B = map(int, input().split())
    K += A - B
    
print('비와이')