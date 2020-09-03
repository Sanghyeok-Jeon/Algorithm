def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        b1 = str(bin(arr1[i])[2:].zfill(n))
        b2 = str(bin(arr2[i])[2:].zfill(n))
        sum_b = ''
        for j in range(n):
            if b1[j] == '1' or b2[j] == '1':
                sum_b += '#'
            else:
                sum_b += ' '
        answer.append(sum_b)
    return answer