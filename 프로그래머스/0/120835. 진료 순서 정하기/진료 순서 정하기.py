def solution(emergency):
    sorted_list = sorted(emergency, reverse=True)  
    return [sorted_list.index(x) + 1 for x in emergency]
