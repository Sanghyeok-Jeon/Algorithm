import sys
sys.stdin = open('BOJ_10773.txt', 'r')

K = int(sys.stdin.readline())

jangbu = []
for n in map(int, sys.stdin):
    if not n:
        jangbu.pop()
    else:
        jangbu.append(n)

print(sum(jangbu))