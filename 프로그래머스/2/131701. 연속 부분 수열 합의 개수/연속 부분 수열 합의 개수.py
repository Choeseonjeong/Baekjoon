def solution(elements):
    cir = set()
    num = len(elements)
    element = elements*2
    for i in range(num):
        for j in range(num):
            cir.add(sum(element[j:j+i+1]))
    return len(cir)
