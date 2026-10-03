#program1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
head=node1
print(node1.data)
print(node2.data)
print(node3.data)
print(node1.next.data)
print(node2.next.data) 
print(node3.next) 
print(head.data)
print(head.next.data)
print(head.next.next.data)
current=head
while current is not None:
    print(current.data)
    current=current.next

#program2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1=Node(5)
node2=Node(15)
node3=Node(25)
node4=Node(35)
node1.next=node2
node2.next=node3
node3.next=node4
head=node1
current=head
while current is not None:
    print(current.data)
    current=current.next