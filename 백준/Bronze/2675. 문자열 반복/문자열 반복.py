n = int(input())
for i in range(n):
    result = ''
    repeat_Num, text = input().split(" ")
    for i in list(text):
        result+=i*int(repeat_Num)
    print(result)