def solution(A):
    disc = []
    for idx, val in enumerate(A):
        disc.append((idx - val, -1))
        disc.append((idx + val, 1))
    disc.sort()

    intersect = 0
    intervals = 0
    for d in disc:
        if d[1] == 1:
            intervals -= 1
        else:
            intersect += intervals
            intervals += 1

    return -1 if intersect > 10000000 else intersect