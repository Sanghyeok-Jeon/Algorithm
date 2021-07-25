import sys
sys.stdin = open('BOJ_19944.txt', 'r')

N, M = map(int, input().split())
if M < 3:
    print('NEWBIE!')
elif M <= N:
    print('OLDBIE!')
else:
    print('TLE!')