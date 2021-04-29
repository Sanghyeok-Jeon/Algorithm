import sys
sys.stdin = open('BOJ_2755.txt', 'r')

N = int(input())
dicGrade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7
          , 'B+': 3.3, 'B0': 3.0, 'B-': 2.7
          , 'C+': 2.3, 'C0': 2.0, 'C-': 1.7
          , 'D+': 1.3, 'D0': 1.0, 'D-': 0.7
          , 'F' : 0.0}

sumScore = 0
sumCredit = 0
for _ in range(N):
    subject, credit, grade = input().split()
    sumScore += int(credit) * dicGrade[grade]
    sumCredit += int(credit)

print("{:.02f}".format(sumScore/sumCredit + (0.001 if sumScore/sumCredit*100%10 >= 5 else 0.000)))