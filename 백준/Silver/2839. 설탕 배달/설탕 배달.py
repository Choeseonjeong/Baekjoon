n = int(input())
k = []
for i in range(n + 1):
    for j in range(n + 1):
        if i * 5 + j * 3 == n:
            k.append(i + j)
        else:
            0

if len(k) == 0:
    print(-1)
else:
    print(min(k))
