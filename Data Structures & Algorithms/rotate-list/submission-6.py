# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        arr=[]
        temp=head
        while temp:
            arr.append(temp)
            temp=temp.next
        n=len(arr)
        k%=n
        if k==0:
            return head
        arr[-1].next=arr[0]
        arr[n-k-1].next=None
        return arr[n-k]