# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
       
        if head is None:
            return head
        else:
            itr = head
            while itr:
                if itr.next is not None:
                    if itr.next.next is not None:
                        if itr.next.val==itr.next.next.val:
                            if itr.next.next.next is not None:
                                itr.next = itr.next.next.next
                            else:
                                itr.next = None
                        else:
                            itr = itr.next
                    else:
                        itr = itr.enex
                else:
                    break
                    
                
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            temp_head = ListNode()
            temp_head.next= head
            itr =temp_head
            while itr:
                if itr.next is not None:
                    while itr.val==itr.next.val:
                        itr.next = itr.next.next
                    
                    itr = itr.next
                else:
                    break
                    
                
        return temp_head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
       
        if head is None:
            return head
        else:
            temp_head = ListNode()
            temp_head.next= head
            itr =temp_head
            while itr:
                if itr.next is not None:
                    if itr.next.next is not None:
                        if itr.next.val==itr.next.next.val:
                            while itr.next.next:
                                if itr.next.val==itr.next.next.val:
                                    itr.next = itr.next.next
                                else:
                                    break
                            itr.next = itr.next.next
                        else:
                            itr = itr.next
                    else:
                        itr = itr.next
    
                else:
                    break
                    
                
        return temp_head.next
                