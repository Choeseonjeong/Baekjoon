def solution(quiz):
    answer = []
    for word in quiz:
        arr = [eval(i.strip()) for i in word.split("=")]
        if arr[0] == arr[1]:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer