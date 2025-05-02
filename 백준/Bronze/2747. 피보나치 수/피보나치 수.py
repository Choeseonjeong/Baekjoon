import sys

num = int(sys.stdin.readline())
b = 1
a = 0
for i in range(num):
  a, b = b, a + b
print(a)