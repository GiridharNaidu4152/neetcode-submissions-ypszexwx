# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        returntemp=ListNode(-8,head)
        temp=returntemp
        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return returntemp.next
        
        