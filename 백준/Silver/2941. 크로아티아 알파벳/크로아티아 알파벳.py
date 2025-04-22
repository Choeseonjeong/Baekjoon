text = input()
arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in arr:
    text = text.replace(i, "*")
print(len(text))