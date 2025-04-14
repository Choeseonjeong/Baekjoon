a,b,c = map(int,input().split(" "))
arr = [a,b,c]
arr.sort()
result = ''
for i in arr:
    result += str(i)  
    result += ' '
print(result)