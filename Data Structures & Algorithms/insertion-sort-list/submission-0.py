# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp)
            temp=temp.next
        arr=sorted(arr,key=lambda node: node.val)
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return arr[0]