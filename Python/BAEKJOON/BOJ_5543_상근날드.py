import sys
sys.stdin = open('BOJ_5543.txt', 'r')

sdBurger = int(input()) - 50
jdBurger = int(input()) - 50
hdBurger = int(input()) - 50
coke = int(input())
cider = int(input())

print(min(sdBurger, jdBurger, hdBurger) + min(coke, cider))