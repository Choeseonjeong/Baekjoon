n = list(map(int,input()))
n.sort(reverse=True)
result = ''
for i in n:
    result+=str(i)
print(result)