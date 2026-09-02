# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        L1,L2=headA,headB
        while L1!=L2:
            L1=L1.next if L1 else headB
            L2=L2.next if L2 else headA
        return L1 