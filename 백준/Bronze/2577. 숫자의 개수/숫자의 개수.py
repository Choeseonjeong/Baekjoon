import sys

num = 1
for i in range(3):
   num *= int(sys.stdin.readline())

num = list(int(i) for i in str(num))

for i in range(10):
    print(num.count(i))