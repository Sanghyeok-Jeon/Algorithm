import sys
sys.stdin = open('BOJ_10987.txt', 'r')

S = input()

cntVowel = 0
for s in S:
    if s in ['a', 'e', 'i', 'o', 'u']:
        cntVowel += 1

print(cntVowel)