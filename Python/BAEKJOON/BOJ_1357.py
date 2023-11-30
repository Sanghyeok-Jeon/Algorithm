import sys
sys.stdin = open('BOJ_1357.txt', 'r')

X, Y = input().split()
Rev = str(int(X[::-1]) + int(Y[::-1]))
print(int(Rev[::-1]))