arr = []
while True:
    line = input()
    if line == '#':
        break
    arr.append(list(line.lower()))
    
    
ret = ["a","e","i","o","u"]
answer = 0

for text in arr:
    answer = 0
    for word in text:
        if word in ret:
            answer+=1
    print(answer)
    
        