import sys
sys.stdin = open('BOJ_6749.txt', 'r')

young = int(input())
middle = int(input())
print(middle * 2 - young)