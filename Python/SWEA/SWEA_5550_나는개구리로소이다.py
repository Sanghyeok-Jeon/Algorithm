import sys
sys.stdin = open('SWEA_5550.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()
    sound = 'croak'
    cntSound = [0] * 5
    frog = 0
    impossible = 0

    for i in range(len(data)):
        frog = max(cntSound[0], frog)
        for j in range(5):
            if data[i] == sound[j]:
                cntSound[j] += 1
                if j and cntSound[j] > cntSound[j-1]:
                    impossible = 1
                    break
                if j == 4:
                    for k in range(5):
                        cntSound[k] -= 1

    if sum(cntSound):
        impossible = 1

    print('#{} {}'.format(tc+1, frog if impossible == 0 else -1))