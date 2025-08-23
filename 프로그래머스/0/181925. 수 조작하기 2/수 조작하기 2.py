def solution(numLog):
    answer = {1:"w",-1:"s",10:"d",-10:"a"}
    word = ""
    for i in range(1,len(numLog)):
        num = numLog[i]-numLog[i-1]
        word+=answer[num]
    return word