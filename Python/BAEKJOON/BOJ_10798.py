import sys
sys.stdin = open('BOJ_10798.txt', 'r')

answer = ['' for _ in range(15)]
for _ in range(5):
    tmpStr = list(input())
    for i in range(len(tmpStr)):
        answer[i] += tmpStr[i]

print(''.join(answer))