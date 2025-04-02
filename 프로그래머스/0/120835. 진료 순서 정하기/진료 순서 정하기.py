def solution(emergency):
    arr = {}
    answer = []
    emergencyArr = sorted(emergency,reverse=True)
    
    for i in range(len(emergencyArr)):
         arr[emergencyArr[i]] = i + 1
        
    for num in emergency:
        answer.append(arr[num])
    return answer