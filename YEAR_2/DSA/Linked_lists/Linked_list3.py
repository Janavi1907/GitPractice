# #Program1
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(5)
# node2=Node(10)
# node3=Node(15)
# node4=Node(20)
# node1.next=node2
# node2.next=node3
# node3.next=node4
# head=node1
# head=head.next
# current=head
# while current is not None:
#     print(current.data)
#     current=current.next

# #Program2
# head=node1
# current=head
# while current is not None:
#     if current.data==10:
#         current.next=current.next.next
#         break
#     current=current.next
# print("After deleting 15:")
# current=head
# while current is not None:
#     print(current.data)
#     current=current.next

#Program3
# class Node1:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node1(5)
# node2=Node1(10)
# node3=Node1(20)
# node4=Node1(30)
# node1.next=node2
# node2.next=node3
# node3.next=node4
# head=node1
# current=head
# while current.next.next is not None:
#     current=current.next
# current.next=None
# current=head
# while current is not None:
#     print(current.data)
#     current=current.next

#Program4
class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node2(10)
node2=Node2(20)
node3=Node2(30)
node1.next=node2
node2.next=node3
head=node1
new_node=Node2(5)
new_node.next=head
head=new_node
new_node1=Node2(40)
current=head
while current.next is not None:
    current=current.next
current.next=new_node1
current=head
while current is not None:
    if current.data==10:
        current.next=current.next.next
        break
    current=current.next
current=head
while current is not None:
    print(current.data)
    current=current.next