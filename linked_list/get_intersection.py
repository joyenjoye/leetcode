# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        else:
            itr1 = headA
            while itr1:
                itr2 = headB
                while itr2:
                    if itr1==itr2:
                         return itr1
                    itr2 = itr2.next
                itr1 = itr1.next    
        return None