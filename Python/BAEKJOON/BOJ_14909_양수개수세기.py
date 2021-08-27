import sys
sys.stdin = open('BOJ_14909.txt', 'r')

print(len(list(filter(lambda x: int(x)>0, sys.stdin.readline().split()))))