str = input()
answer = ''
for word in str:
    if word.isupper():
        answer+=word.lower()
    else:
        answer+=word.upper()
print(answer)