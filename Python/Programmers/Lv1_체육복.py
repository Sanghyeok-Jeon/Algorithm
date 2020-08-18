def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lostSelect = [0] * len(lost)
    reserveSelect = [0] * len(reserve)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lostSelect[i] = 1
                reserveSelect[j] = 1

    for i in range(len(lost)):
        if lostSelect[i]:
            continue
        for j in range(len(reserve)):
            if reserveSelect[j]:
                continue
            if lost[i] == reserve[j] - 1 or lost[i] == reserve[j] + 1:
                reserveSelect[j] = 1
                lostSelect[i] = 1
                break

    answer += n - lostSelect.count(0)
    return answer