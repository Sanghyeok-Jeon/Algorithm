import sys
import collections
sys.stdin = open('BOJ_9019.txt', 'r')
input = sys.stdin.readline

def BFS():
    q = collections.deque()
    q.append((A, ""))

    while q:
        number, command = q.popleft()

        resultD = (number * 2) % 10000
        if resultD == B:
            return command + "D"
        elif not visited[resultD]:
            visited[resultD] = 1
            q.append((resultD, command + "D"))

        resultS = number - 1 if number else 9999
        if resultS == B:
            return command + "S"
        elif not visited[resultS]:
            visited[resultS] = 1
            q.append((resultS, command + "S"))

        resultL = number % 1000 * 10 + number // 1000
        if resultL == B:
            return command + "L"
        elif not visited[resultL]:
            visited[resultL] = 1
            q.append((resultL, command + "L"))

        resultR = number % 10 * 1000 + number // 10
        if resultR == B:
            return command + "R"
        elif not visited[resultR]:
            visited[resultR] = 1
            q.append((resultR, command + "R"))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000

    print(BFS())