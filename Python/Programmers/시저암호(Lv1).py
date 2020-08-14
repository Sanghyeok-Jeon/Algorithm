#1
def solution(s, n):
    data = list(s)
    for i in range(len(data)):
        if ord('a') <= ord(data[i]) <= ord('z'):
            data[i] = chr(ord(data[i])+n) if ord(data[i]) + n <= ord('z') else chr((ord(data[i])+n-1)%ord('z') + ord('a'))
        if ord('A') <= ord(data[i]) <= ord('Z'):
            data[i] = chr(ord(data[i])+n) if ord(data[i]) + n <= ord('Z') else chr((ord(data[i])+n-1)%ord('Z') + ord('A'))
    answer = ''.join(data)
    return answer

#2
def solution(s, n):
    data = list(s)
    for i in range(len(data)):
        if ord('a') <= ord(data[i]) <= ord('z'):
            data[i] = chr((ord(data[i])-ord('a')+n)%26 + ord('a'))
        if ord('A') <= ord(data[i]) <= ord('Z'):
            data[i] = chr((ord(data[i])-ord('A')+n)%26 + ord('A'))
    answer = ''.join(data)
    return answer