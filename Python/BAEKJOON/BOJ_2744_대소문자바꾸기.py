import sys
sys.stdin = open('BOJ_2744.txt', 'r')

data = input()
result = ''
for d in data:
    if d.islower():
        result += d.upper()
    else:
        result += d.lower()

print(result)