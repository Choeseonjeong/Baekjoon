def is_prime(n):
    arr = []
    for i in range(1,n+1):
        if n % i == 0:
            arr.append(i)
    return arr

answer = []
while True:
    answer.append(list(map(int,input().split())))
    if answer[-1]==[0,0]:
        answer = answer[:-1]
        break
    
for i in answer:
    if i[0] > i[1]:
       if i[1] in is_prime(i[0]):
           print("multiple")
       else:
           print("neither")
    else:
        if i[1] % i[0] == 0:
            print("factor")
        else:
            print("neither")

