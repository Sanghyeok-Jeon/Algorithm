import sys
sys.stdin = open('BOJ_2751.txt', 'r')

N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]
for n in sorted(data):
    print(n)