s = "adc"
def resultingString(s):
    stack = []
    for c in s:
        
        if len(stack) == 0:
            stack.append(c)
            print(stack)
            continue
        top = stack.pop()
        print(stack, "top = ",top,"c =",c)
        if (ord(top) - ord(c))% 26 == 1 or (ord(c) - ord(top)) % 26 == 1:
            print(top,c, ord(top),ord(c))
            continue
        else:
            stack.append(top)
            stack.append(c)
            print(stack)
    ans = ""
    for c in stack:
        ans+=c
    print(ans)

resultingString(s)
#adcb