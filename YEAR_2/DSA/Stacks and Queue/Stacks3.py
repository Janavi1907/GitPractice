#Task 1
text = "(())"
stack=[]
for i in text:
    if i=="(":
        stack.append(i)
    elif i==")":
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not balanced")

#Task 2
text = "(()"
stack=[]
for i in text:
    if i=="(":
        stack.append(i)
    elif i==")":
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not balanced")

#Task 3
text = "())("
stack=[]
for i in text:
    if i=="(":
        stack.append(i)
    elif i==")":
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not balanced")

#Mini Challenge 
text = "((()))"
stack=[]
for i in text:
    if i=="(":
        stack.append(i)
    elif i==")":
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not balanced")
text = "(()())"
stack=[]
for i in text:
    if i=="(":
        stack.append(i)
    elif i==")":
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not balanced")


