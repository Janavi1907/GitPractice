#program1
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
head=node1
new_node=Node(5)
new_node.next=head
head=new_node
current=head
while current is not None:
    print(current.data)
    current=current.next

#Program2
new_node=Node(40)
current=head
while current.next is not None:
    current=current.next
current.next=new_node
print("After inserting 40 at the end:")
current=head
while current is not None:
    print(current.data)
    current=current.next

#Program3
new_node=Node(15)
current=head
while current is not None:
    if current.data==10:
        new_node.next=current.next
        current.next=new_node
        break
    current=current.next
print("After inserting 15 after 10:")
current=head
while current is not None:
    print(current.data)
    current=current.next

