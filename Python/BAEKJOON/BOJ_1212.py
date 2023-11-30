import sys
sys.stdin = open('BOJ_1212.txt', 'r')

## 1
# octalNum = input()
# octTobin = ['000', '001', '010', '011', '100', '101', '110', '111']
#
# answer = ''
# lenOctalNum = len(octalNum)
# for i in range(lenOctalNum):
#     if i == 0:
#         if octalNum[i] == '0':
#             answer += '0'
#             break
#         elif octalNum[i] == '1':
#             answer += '1'
#         elif octalNum[i] == '2':
#             answer += '10'
#         elif octalNum[i] == '3':
#             answer += '11'
#         else:
#             answer += octTobin[int(octalNum[i])]
#     else:
#         answer += octTobin[int(octalNum[i])]
#
# print(answer)

print(format(int(input(), 8), 'b'))
