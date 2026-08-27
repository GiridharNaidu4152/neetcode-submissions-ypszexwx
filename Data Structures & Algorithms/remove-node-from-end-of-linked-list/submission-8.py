# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        temp=head
        while temp:
            nodes.append(temp)
            temp=temp.next
        if n==len(nodes):
            return nodes[-n].next
        elif n==1:
            nodes[-2].next=None
            return head
        nodes[-(n+1)].next=nodes[-(n-1)]
        return head