import collections

def solution(priorities, location):
    answer = 0
    q = collections.deque([(v, i) for i, v in enumerate(priorities)])

    while q:
        document = q.popleft()
        if q and max(q)[0] > document[0]:
            q.append(document)
        else:
            answer += 1
            if document[1] == location:
                break

    return answer