arr = [] 
for i in range(28): 
    n = int(input()) 
    arr.append(n) 

for i in range(1, 31): 
    if i not in arr: 
        print(i)
