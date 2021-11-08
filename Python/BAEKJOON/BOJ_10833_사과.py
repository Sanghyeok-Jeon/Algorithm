import sys
sys.stdin = open('BOJ_10833.txt' , 'r')

N = int(input())
result = 0
for _ in range(N):
    student, apple = map(int, input().split())
    result += apple % student
print(result)