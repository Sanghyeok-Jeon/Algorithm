import sys
sys.stdin = open('BOJ_4766.txt', 'r')

oldTemperature = 999

while True:
    temperature = float(input())
    if temperature == 999:
        break

    if oldTemperature != 999:
        print("{:.2f}".format(temperature - oldTemperature))

    oldTemperature = temperature