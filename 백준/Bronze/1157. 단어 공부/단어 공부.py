words = input().upper()
num = list(set(words))
cnt_list = []
for i in num:
    cnt = words.count(i)
    cnt_list.append(cnt)


if cnt_list.count(max(cnt_list))>1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  
    print(num[max_index])