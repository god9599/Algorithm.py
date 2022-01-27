from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for i in range(bridge_length)])
    total_weight = 0
    cnt = 0
    truck_weights.sort(reverse=True)

    while truck_weights:
        total_weight -= bridge.popleft()

        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            _truck = truck_weights.pop()
            bridge.append(_truck)
            total_weight += _truck
        cnt += 1

    cnt += bridge_length
    return cnt
