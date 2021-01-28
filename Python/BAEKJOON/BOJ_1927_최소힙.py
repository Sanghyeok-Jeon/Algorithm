import sys
import heapq
sys.stdin = open('BOJ_1927.txt', 'r')

N = int(sys.stdin.readline())
X = []

i = 0
while i < N:
    n = int(sys.stdin.readline().rstrip())
    if n:
        heapq.heappush(X, n)
    else:
        if X:
            print(heapq.heappop(X))
        else:
            print(0)
    i += 1