import sys
sys.stdin = open('2050.txt', 'r')

data = input()

for c in data:
    print(ord(c)-ord('A')+1, end=' ')