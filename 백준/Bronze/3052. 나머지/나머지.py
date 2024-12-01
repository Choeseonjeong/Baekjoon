arr = []
for i in range(10):
    n = (int(input()))%42
    arr.append(n)

print(len(set(arr)))