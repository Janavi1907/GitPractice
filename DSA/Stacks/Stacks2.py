#Task 1
stack=[]
word = "Python"
for i in word:
    stack.append(i)
for i in word:
    popped_element=stack.pop()
    print(popped_element,end="")

#Task 2
stack = [10, 20, 30, 40, 50]
popped_element1=stack.pop()
popped_element2=stack.pop()
print("Removed:",popped_element1)
print("Removed:",popped_element2)
print("Remaining:",stack)

#Task 3
stack = [10, 20, 30]
while True:
    if len(stack)==0:
        print("Stack is empty")
        break
    popped_element=stack.pop()
    print(popped_element)

#Task 4
stack = []
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)
stack.pop()
stack.append(25)
print("Top element:",stack[-1])
print(stack)
