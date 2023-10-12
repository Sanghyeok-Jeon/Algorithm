import sys
sys.stdin = open('BOJ_25192.txt', 'r')

N = int(input())
cntGomGom = 0

setUser = set()
for i in range(N):
    chat = input()
    if chat == 'ENTER':
        cntGomGom += len(setUser)
        setUser.clear()
    else:
        setUser.add(chat)

cntGomGom += len(setUser)

print(cntGomGom)