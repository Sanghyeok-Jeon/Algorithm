import sys
import heapq
sys.stdin = open('BOJ_11286.txt', 'r')

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)