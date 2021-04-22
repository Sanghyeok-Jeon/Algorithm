import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = collections.deque([0] * bridge_length)
    truckWeights = collections.deque(truck_weights)
    onBridgeWeight = 0

    while q:
        answer += 1
        nowTruck = q.popleft()
        if nowTruck:
            onBridgeWeight -= nowTruck

        if truckWeights:
            if onBridgeWeight + truckWeights[0] > weight:
                q.append(0)
            else:
                nextTruck = truckWeights.popleft()
                q.append(nextTruck)
                onBridgeWeight += nextTruck

    return answer