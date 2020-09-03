def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7, '*']
    middle = [2, 5, 8, 0]
    right = [3, 6, 9, '#']

    l = [3, 0]
    r = [3, 2]
    for i in range(len(numbers)):
        if numbers[i] in left:
            for j in range(4):
                if left[j] == numbers[i]:
                    l = [j, 0]
                    break
            answer += 'L'
        elif numbers[i] in right:
            for j in range(4):
                if right[j] == numbers[i]:
                    r = [j, 2]
                    break
            answer += 'R'
        else:
            for j in range(4):
                if middle[j] == numbers[i]:
                    if abs(l[0] - j) + abs(l[1] - 1) > abs(r[0] - j) + abs(r[1] - 1):
                        answer += 'R'
                        r = [j, 1]
                        break
                    elif abs(l[0] - j) + abs(l[1] - 1) < abs(r[0] - j) + abs(r[1] - 1):
                        answer += 'L'
                        l = [j, 1]
                        break
                    else:
                        if hand == 'left':
                            answer += 'L'
                            l = [j, 1]
                            break
                        else:
                            answer += 'R'
                            r = [j, 1]
                            break

    return answer