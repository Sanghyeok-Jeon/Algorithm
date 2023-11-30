import sys
sys.stdin = open('BOJ_3046.txt', 'r')

R1, S = map(int, input().split())
print(2*S - R1)