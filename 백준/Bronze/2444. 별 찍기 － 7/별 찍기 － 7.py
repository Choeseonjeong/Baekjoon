n = int(input())

for i in range(1,n+1):
    num = n-i
    print(" "*num+"*"*(i*2-1))
for i in range(n-1,0,-1):
    num = n-i
    print(" "*num+"*"*(i*2-1))

