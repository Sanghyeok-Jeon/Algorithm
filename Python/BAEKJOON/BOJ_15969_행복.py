import sys
sys.stdin = open('BOJ_15969.txt', 'r')

N = int(input())
score = list(map(int, input().split()))

print(max(score) - min(score))