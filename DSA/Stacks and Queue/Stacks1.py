#Task 1
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

#Task 2
stack = [10, 20, 30, 40]
stack_pop1=stack.pop()
stack_pop2=stack.pop()
print("Removed:",stack_pop1)
print("Removed:",stack_pop2)
print("Remaining:",stack)

#Task 3
stack = [5, 10, 15, 20]
print("Top element:",stack[-1])

#Task 4
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

#Mini Challenge
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.pop()
stack.append(50)
print("Top element:",stack[-1])
print(stack)