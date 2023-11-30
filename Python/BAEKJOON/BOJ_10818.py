import sys
sys.stdin = open('BOJ_10818.txt', 'r')

N = int(input())
data = list(map(int, input().split()))

print('{} {}'.format(min(data), max(data)))