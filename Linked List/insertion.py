#create a node class 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#create a linked List
class Linked_list:
    #initialize the linkedlist or create the head
    def __init__(self):
        self.head=None
    #function for adding the new_node at the beggining of linked list
    def insert_at_beg(self ,new_data):
        new_node=Node(new_data) 
        new_node.next=self.head

        self.head=new_node

    #function for adding the new_node after a given node of linked list
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print('enter a valid node')
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    #function for adding the new_node at the end  of linked list
    def insert_at_end(self,new_data):
        new_node=Node(new_data)
        
        if self.head is None:
            self.head=new_node
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new_node
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    # *** function for adding the new_node at a given index of linked list
    def insert_at_index(self,new_data,index):
        if index<0 and index>=self.get_length():
            raise Exception('invalid index')
        
            

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                new_node=Node(new_data)
                new_node.next=itr.next
                itr.next=new_node
                break
            itr=itr.next
            count+=1
    

        

        
    #function to print our linked list
    def printList(self):
        itr=self.head
        llist=''
        while itr:
            llist+='['+str(itr.data)+']' +'-->'
            itr=itr.next
        print(llist+'None')

if __name__=='__main__':
    li=Linked_list()
    li.insert_at_beg(7)
    li.insert_at_beg(6)
    li.insert_at_beg(5)
    li.insert_at_end(8)
    li.insert_after(li.head.next.next,7.5)
    li.insert_at_index(6.5,12)
    li.printList()