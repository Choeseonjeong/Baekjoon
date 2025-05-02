import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    text = sys.stdin.readline().split()
    if text[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
    elif text[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    
    elif text[0] == "size":
        print(len(stack))
    
    elif text[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    
    elif text[0] == "push":
        stack.append(text[1])
        
