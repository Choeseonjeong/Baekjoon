a, b = list(map(int, input().split()))
c = []
sum1 = int(str(a).replace("5", "6")) + int(str(b).replace("5", "6"))
sum2 = int(str(a).replace("5", "6")) + int(str(b).replace("6", "5"))
sum3 = int(str(a).replace("6", "5")) + int(str(b).replace("5", "6"))
sum4 = int(str(a).replace("6", "5")) + int(str(b).replace("6", "5"))

c.append(sum1)
c.append(sum2)
c.append(sum3)
c.append(sum4)

c.sort()

print(c[0], c[3])
