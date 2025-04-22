times = 0
answer = 0
dic = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}

for i in range(20):
    name,time,score = input().split()
    if score in dic:
        times += float(time)
        answer += (dic[score])*float(time)
print(round(answer/times,6))
    