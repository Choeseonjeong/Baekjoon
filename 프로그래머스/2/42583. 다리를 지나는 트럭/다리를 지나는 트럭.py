def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    current_weight = 0
    
    while len(truck_weights) > 0:
        time += 1
        current_weight = current_weight- bridge.pop(0)
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    time+=bridge_length
    return time
        