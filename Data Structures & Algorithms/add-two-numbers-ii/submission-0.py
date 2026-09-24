# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        arr1=[]
        while temp1:
            arr1.append(temp1.val)
            temp1=temp1.next
        temp2=l2
        arr2=[]
        while temp2:
            arr2.append(temp2.val)
            temp2=temp2.next
        carry=0
        head=None
        while arr1 or arr2 or carry:
            v1=arr1.pop() if arr1 else 0
            v2=arr2.pop() if arr2 else 0
            add=v1+v2+carry
            carry=0
            if add>=10:
                carry=1
                add-=10
            temp=ListNode(add)
            temp.next=head
            head=temp
        return head