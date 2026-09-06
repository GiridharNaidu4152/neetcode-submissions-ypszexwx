# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        left,right=head,prev
        max=0
        while right:
            if right.val+left.val>max:
                max=right.val+left.val
            right=right.next
            left=left.next
        return max