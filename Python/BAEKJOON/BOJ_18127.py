import sys
sys.stdin = open('BOJ_18127.txt', 'r')

A, B = map(int, input().split())
print(1*(B+1) + (A-2)*B*(B+1)//2)