n = int(input())
arr=[]
for i in range(n):
    age,name = input().split()
    arr.append((int(age), name, i)) 
arr.sort(key=lambda x : (int(x[0]),x[2]))
for i in arr:
    print(i[0],i[1])