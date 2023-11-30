import sys
sys.stdin = open('BOJ_1436.txt', 'r')

N = int(input())
movieName = 666
cnt = 0
while True:
    if '666' in str(movieName):
        cnt += 1
    if cnt == N:
        print(movieName)
        break
    movieName += 1