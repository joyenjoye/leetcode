# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
            
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            node = None
            itr1 = list1
            itr2 = list2
            k = 0
            while True:
                if itr1.val<=itr2.val:
                    val = itr1.val
                    if node is None:
                        node = ListNode(val)
                    else:
                        itr = node
                        while itr:
                            if itr.next is None:
                                itr.next = ListNode(val)
                                break
                            itr = itr.next
                            
                    if itr1.next is not None:
                        itr1 = itr1.next
                    else:
                        itr = node
                        while itr:
                            if itr.next is None:
                                itr.next = itr2
                                break
                            itr = itr.next
                        return node
                else:
                    val = itr2.val
                    if node is None:
                        node = ListNode(val)
                    else:
                        itr = node
                        while itr:
                            if itr.next is None:
                                itr.next = ListNode(val)
                                break
                            itr = itr.next
                        
                    if itr2.next is not None:
                        itr2 = itr2.next
                    else:
                        itr = node
                        while itr:
                            if itr.next is None:
                                itr.next = itr1
                                break
                            itr = itr.next
                        return node
                    
        return node