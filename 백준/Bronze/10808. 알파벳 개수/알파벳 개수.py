import sys

text = sys.stdin.readline().strip()

word='abcdefghijklmnopqrstuvwxyz'
dic = {}

for i in list(word):
    dic[i] = 0

for i in text:
    if i in dic:
        dic[i]+=1
        
for idx, value in dic.items():
    print(value,end=' ')