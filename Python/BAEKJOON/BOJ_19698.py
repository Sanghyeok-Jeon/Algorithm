import sys
sys.stdin = open('BOJ_19698.txt', 'r')

N, W, H, L = map(int, input().split())
possible = (W//L) * (H//L)
print(min(N, possible))