import sys
sys.stdin = open('BOJ_2587.txt', 'r')

data = sorted(list(map(int, sys.stdin.readlines())))
print(sum(data)//5)
print(data[2])