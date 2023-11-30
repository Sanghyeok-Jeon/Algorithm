import sys
sys.stdin = open('BOJ_5596.txt', 'r')

mingook = sum(map(int, input().split()))
manse = sum(map(int, input().split()))

print(mingook if mingook >= manse else manse)