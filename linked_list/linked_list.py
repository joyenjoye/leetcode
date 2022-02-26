

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        linked_list_str = ""

        while itr:
            linked_list_str += str(itr.data)+"->"
            itr = itr.next
        print(linked_list_str)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = Node(data,None)
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head = self.head.next
            return 
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_begining(data)
            return 

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1

    
if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.insert_at_begining(1)
    my_linked_list.insert_at_begining(2)
    my_linked_list.insert_at_end(3)
    my_linked_list.insert_values(["you","are","cute"])
    my_linked_list.print()
    print(my_linked_list.get_length())
    my_linked_list.remove_at(2)
    my_linked_list.insert_at(2,"I am happy")
    my_linked_list.print()
