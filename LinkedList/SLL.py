class Node:
    def __init__(self,val):
        self.val =val
        self.next =None
node1=Node(5)
node2=Node(6)
node1.next=node2
print(node2)
print(node1.next)