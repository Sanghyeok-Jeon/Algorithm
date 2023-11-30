import sys
sys.stdin = open('BOJ_20492.txt', 'r')

N = int(input())
print(int(N*0.78), int(N*(1-0.2*0.22)))