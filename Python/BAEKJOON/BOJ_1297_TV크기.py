import sys
sys.stdin = open('BOJ_1297.txt', 'r')

d, heightRatio, widthRatio = map(int, input().split())

height = d / (heightRatio**2 + widthRatio**2)**0.5

print('{} {}'.format(int(heightRatio*height), int(widthRatio*height)))