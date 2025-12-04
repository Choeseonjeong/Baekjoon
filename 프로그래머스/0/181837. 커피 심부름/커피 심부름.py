def solution(order):
    charge = 0
    a = ["iceamericano", "americanoice","hotamericano", "americanohot""americano","anything","americano"]
    b = ["icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot","cafelatte"]
    
    for word in order:
        if word in a:
            charge+=4500
        elif word in b:
            charge += 5000
        else:
            charge+=4500
    return charge