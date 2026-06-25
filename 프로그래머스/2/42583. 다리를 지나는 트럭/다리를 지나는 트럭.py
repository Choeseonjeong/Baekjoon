from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    while len(truck_weights) != 0:
        time += 1
        bridge.pop(0)
        
        if truck_weights[0] + sum(bridge) <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    time += bridge_length
    return time