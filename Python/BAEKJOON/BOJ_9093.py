import sys
sys.stdin = open('BOJ_9093.txt', 'r')

T = int(input())
for tc in range(T):
    print(' '.join(word[::-1] for word in input().split()))