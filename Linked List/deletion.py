class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertion(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    #function to delete the node at starting
    def delete_at_beg(self):
        self.head=self.head.next
    
    #counter function to count the length of lilist
    def get_count(self):
        count=0
        itr=self.head 
        while itr:
            count+=1
            itr=itr.next
        return count
    #function to delete the node at the given index
    def delete_at_index(self,index):
        if index<0 or index>=self.get_count():
            print('enter a valid index')
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            count+=1
            itr=itr.next

    def printList(self):
        if self.head is None:

            print('list is empty')
            return
        itr=self.head
        lilist=''
        while itr:
            lilist+=str(itr.data)+'-->'
            itr=itr.next
        print(lilist+'None')
        
if __name__ =='__main__':
    li=LinkedList()
    li.insertion(5)
    li.insertion(6)
    li.insertion(7)
    li.insertion(8)
    li.printList()
    li.delete_at_beg()
    li.printList()
    li.delete_at_index(1)
    li.printList()
