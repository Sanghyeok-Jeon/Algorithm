import sys
sys.stdin = open('BOJ_10569.txt', 'r')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    print(2 + E - V)