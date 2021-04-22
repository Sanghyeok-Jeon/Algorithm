import collections

def solution(progresses, speeds):
    answer = []
    qProgress = collections.deque(progresses)
    qSpeed = collections.deque(speeds)
    time = 0
    cnt = 0

    while qProgress:
        if qProgress[0] + time * qSpeed[0] >= 100:
            qProgress.popleft()
            qSpeed.popleft()
            cnt += 1
        else:
            if cnt:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)

    return answer