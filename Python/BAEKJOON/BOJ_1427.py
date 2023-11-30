import sys
sys.stdin = open('BOJ_1427.txt', 'r')

print(''.join(sorted(input())[::-1]))