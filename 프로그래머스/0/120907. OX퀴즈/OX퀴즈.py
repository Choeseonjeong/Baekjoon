def solution(quiz):
    arr = []
    for text in quiz:
        if eval(text.split(" = ")[0]) == int(text.split(" = ")[1]):
            arr.append("O")
        else:
            arr.append("X")
    return arr