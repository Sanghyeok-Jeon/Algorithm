import sys
sys.stdin = open('BOJ_2752.txt', 'r')

print(*sorted(map(int, input().split())))