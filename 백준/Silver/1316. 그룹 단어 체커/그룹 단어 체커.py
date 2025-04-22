n = int(input())
arr = [input() for i in range(n)]

def groupText(text):
    answer = set()
    prev = ''
    for char in text:
        if char != prev:
            if char in answer:
                return False
            answer.add(char)
        prev = char
    return True

            
count = 0
for text in arr:
    count+=groupText(text)
print(count)