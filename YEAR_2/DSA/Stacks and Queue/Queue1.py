#Task 1
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print(queue)

#Task 2
queue = [10, 20, 30, 40]
first_removed=queue.pop(0)
second_removed=queue.pop(0)
print("First removed:",first_removed)
print("Second removed:",second_removed)
print("Remaining:",queue)

#Task 3
queue = [5, 10, 15, 20]
print("Front:",queue[0])
print("Rear:",queue[-1])

#Task 4
queue = []
if len(queue)==0:
    print("Queue is empty")
else:
    print("Queue is not empty")
queue.append(100)
if len(queue)==0:
    print("Queue is empty")
else:
    print("Queue is not empty")

#Mini Challenge
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
removed_ele1=queue.pop(0)
queue.append(40)
queue.append(50)
removed_ele2=queue.pop(0)
print("Removed:",removed_ele1)
print("Removed:",removed_ele2)
print("Remaining:",queue)
print("Front:",queue[0])
print("Rear:",queue[-1])