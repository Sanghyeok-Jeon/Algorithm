import sys
sys.stdin = open('BOJ_3447.txt', 'r')

while True:
    try:
        data = input()
        replaceData = data.replace('BUG', '')
        while True:
            if data == replaceData:
                break
            data = replaceData
            replaceData = replaceData.replace('BUG', '')
        print(data)
    except:
        break