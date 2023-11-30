import sys
sys.stdin = open('BOJ_10950.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print(A+B)