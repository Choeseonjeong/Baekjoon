import sys
input = sys.stdin.readline

N = int(input())
chat = set()
people = 0
for _ in range(N):
    name = input().rstrip()
    if name == 'ENTER':
        people += len(chat)
        chat.clear()
    else:
        chat.add(name)
people += len(chat)
print(people)
