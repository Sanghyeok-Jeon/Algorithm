import sys
sys.stdin = open('BOJ_10178.txt', 'r')

N = int(input())
for _ in range(N):
    c, v = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(c//v, c%v))