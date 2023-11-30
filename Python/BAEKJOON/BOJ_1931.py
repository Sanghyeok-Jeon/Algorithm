import sys
sys.stdin = open('BOJ_1931.txt', 'r')

N = int(sys.stdin.readline())
meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

ans = 0
start = 0
for m in meeting:
    if m[0] >= start:
        start = m[1]
        ans += 1

print(ans)
print(meeting)