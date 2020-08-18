def solution(s):
    answer = True
    num = ['0', '1', '2', '3', '4', '5', '6' ,'7', '8', '9']
    if len(s) == 6 or len(s) == 4:
        for c in s:
            if c not in num:
                answer = False
                break
    else:
        answer = False
    return answer