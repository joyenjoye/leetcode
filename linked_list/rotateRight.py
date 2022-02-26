    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0 
        if head is None:
            pass
        elif head.next is None:
            pass
        else:
            while count<k:
                itr = head
                while itr:
                    if itr.next.next is None:
                        node = itr.next
                        itr.next = None
                        node.next = head
                        head = node
                        break
                    
                    itr = itr.next
                        
                count = count+1


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            pass
        elif head.next is None:
            pass
        else:
            itr = head
            i = 0
            while itr:
                itr = itr.next
                i = i+1 
            count = 0 
            k = k%i
            while count<k:
                itr = head
                while itr:
                    if itr.next.next is None:
                        node = itr.next
                        itr.next = None
                        node.next = head
                        head = node
                        break
                    
                    itr = itr.next
                        
                count = count+1
 
        return head   