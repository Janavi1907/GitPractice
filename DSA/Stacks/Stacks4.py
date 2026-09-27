#Task 1
word = "Data"
stack=[]
for i in word:
    stack.append(i)
for i in word:
    popped_element=stack.pop()
    print(popped_element,end="")

#task 2
stack = [10, 20, 30, 40]
while True:
    if len(stack)==0:
        print("Stack is empty")
        break
    popped_element=stack.pop()
    print(popped_element)

#Task 3
stack=[]
if len(stack)==0:
    print("Stack is empty")
else:
    print("Stack is not empty")
stack.append(100)
if len(stack)==0:       
    print("Stack is empty")
else:
    print("Stack is not empty")

#task 4
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
popped_element1=stack.pop()
stack.append(40)
stack.append(50)
popped_element2=stack.pop()
stack.append(60)
print(stack)
print("Removed:",popped_element1)
print("Removed:",popped_element2)
print("Top element:",stack[-1])

#Task 5
text="(()())"
stack = []
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
text = "())"
stack = []
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
