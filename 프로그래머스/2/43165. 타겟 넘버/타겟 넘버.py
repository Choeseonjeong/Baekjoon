def solution(numbers, target):
    count = 0
    leaves = [0]
    
    for num in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf-num)
            temp.append(leaf+num)
        leaves = temp
    return leaves.count(target)