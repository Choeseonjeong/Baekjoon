def solution(myString, pat):
    answer = []
    count = 0
    for i in range(len(myString)-len(pat)+1):
        answer.append(myString[i:i+len(pat)])
    for i in answer:
        if i==pat:
            count+=1
    return count