def solution(arr):
    answer = 0
    multiArr = arr[0]
    maxArr = arr[0]
    for i in range(1, len(arr)):
        multiArr *= arr[i]
        maxArr = max(maxArr, arr[i])

    for j in range(maxArr, multiArr + 1):
        possible = 1
        idx = 0

        while idx < len(arr):
            if j % arr[idx]:
                possible = 0
                break
            idx += 1

        if possible:
            answer = j
            break

    return answer