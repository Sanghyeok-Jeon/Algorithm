import sys
sys.stdin = open('BOJ_20540.txt', 'r')

MBTI = input()
LOVE = ''

i = 0
while len(LOVE) < 4:
    if i == 0:
        if MBTI[i] == 'E':
            LOVE += 'I'
        else:
            LOVE += 'E'
    elif i == 1:
        if MBTI[i] == 'N':
            LOVE += 'S'
        else:
            LOVE += 'N'
    elif i == 2:
        if MBTI[i] == 'T':
            LOVE += 'F'
        else:
            LOVE += 'T'
    else:
        if MBTI[i] == 'J':
            LOVE += 'P'
        else:
            LOVE += 'J'
    i += 1

print(LOVE)


#### Wow!!! ####
# a={'E':'I','I':'E','S':'N','N':'S','T':'F','F':'T','J':'P','P':'J'}
# print(''.join([a[i] for i in input()]))