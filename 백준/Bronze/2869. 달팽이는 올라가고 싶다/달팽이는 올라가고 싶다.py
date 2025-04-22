import math
up, down, success = map(int,input().split())
target = success - up
if target<=0:
    print(1)
else:
    print(math.ceil(target / (up - down)) + 1)