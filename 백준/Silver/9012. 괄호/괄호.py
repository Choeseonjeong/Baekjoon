import sys

N = int(sys.stdin.readline())

for i in range(N):
    arr = []
    text = list(sys.stdin.readline().rstrip())
    
    for i in text:
        if i == "(":
            arr.append("(")
        elif i == ")":
            if len(arr)==0:
                arr.append(")")
                break
            else:
                arr.pop()
        
    print("YES" if len(arr)==0 else "NO")

