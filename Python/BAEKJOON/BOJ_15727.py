import sys
sys.stdin = open('BOJ_15727.txt', 'r')

L = int(input())
print(L//5 + 1 if L%5 else L//5)