import sys
sys.stdin = open('BOJ_1075.txt', 'r')

N = input()
F = int(input())

chgN = int(N[:-2] + '00')
while True:
    if not chgN % F:
        break

    chgN += 1

print(str(chgN)[-2:])
