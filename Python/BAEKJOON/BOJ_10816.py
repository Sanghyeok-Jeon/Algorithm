import sys
sys.stdin = open('BOJ_10816.txt', 'r')

N = int(sys.stdin.readline())
cardData = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

dictCard = dict()

for card in cardData:
    try:
        dictCard[card] += 1
    except:
        dictCard[card] = 1

for t in target:
    try:
        print(dictCard[t], end=' ')
    except:
        print(0, end=' ')