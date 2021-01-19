import sys
sys.stdin = open('BOJ_1541.txt', 'r')

# listSum = []
# splitMinus = sys.stdin.readline().split('-')
# for m in splitMinus:
#     tmp = 0
#     splitPlus = m.split('+')
#     for p in splitPlus:
#         tmp += int(p)
#     listSum.append(tmp)

listSum = [sum(map(int, splitMinus.split('+'))) for splitMinus in sys.stdin.readline().split('-')]
print(listSum[0]-sum(listSum[1:]))