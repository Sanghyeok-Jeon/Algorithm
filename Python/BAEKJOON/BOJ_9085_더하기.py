import sys
sys.stdin = open('BOJ_9085.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    print(sum(map(int, input().split())))