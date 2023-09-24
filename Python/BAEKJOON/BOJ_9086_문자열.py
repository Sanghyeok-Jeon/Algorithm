import sys
sys.stdin = open('BOJ_9086.txt', 'r')

T = int(input())
for _ in range(T):
    s = input()
    print(s[0] + s[-1])