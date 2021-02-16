import sys
sys.stdin = open('SWEA_1224.txt', 'r')

isp = {'*':2, '+':1, '(':0}
icp = {'*':2, '+':1, '(':3}

for tc in range(10):
    length = int(input())
    data = input()
    stackData = []
    stackOp = []

    for d in data:
        if d.isdigit():
            stackData.append(d)
        elif d == ')':
            while stackData[-1] != '(':
                stackData.append(stackOp.pop())
            stackData.pop()
        else:
            while stackOp and isp[stackOp[-1]] >= icp[d]:
                stackData.append(stackOp.pop())
            stackOp.append(d)

    stackResult = []
    for sd in stackData:
        if sd == '*':
            stackResult.append(stackResult.pop() * stackResult.pop())
        elif sd == '+':
            stackResult.append(stackResult.pop() + stackResult.pop())
        else:
            stackResult.append(int(sd))

    print('#{} {}'.format(tc+1, stackResult[0]))