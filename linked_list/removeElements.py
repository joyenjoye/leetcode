# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        if self.val is None:
            print("The linked List is empty")
        itr = self.val
        


def removeElements(head: ListNode, val: int) -> ListNode:
    count = 0
    while head.next:
        if count==0 and head.val ==val:
            head.val = head.next
        else:
            count =count+1
    
        if head.next == val:
            head.next = head.next.next
    return head 
                
if __name__ == "__main__":
    head = ListNode()
    removeElements(head,0)
    
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is not None:
            count = 0
            itr = head
            while itr:
                if count==0 and itr.val==val:
                    head = itr.next
                    itr = itr.next
                    continue
                else:
                    count =count+1
            

                if itr.next is None:
                    if itr.val== val:
                        return None
                    break
                else:
                    if itr.next.val == val:
                        itr.next = itr.next.next
                    itr = itr.next
           
        return head 