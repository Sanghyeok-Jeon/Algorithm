data = '0123456789ABCDEF'

def jinsu(num, base):
    q, r = divmod(num, base)
    n = data[r]
    return jinsu(q, base) + n if q else n

def solution(n, t, m, p):
    answer = ''
    lst_number = ''
    for i in range(t * m):
        lst_number += jinsu(i, n)

    for i in range(p - 1, t * m, m):
        answer += lst_number[i]

    return answer