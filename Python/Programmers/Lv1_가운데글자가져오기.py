def solution(s):
    data = s
    if len(data) % 2:
        answer = data[len(data)//2]
    else:
        answer = data[len(data)//2-1:len(data)//2+1]
    return answer