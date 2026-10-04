# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        arr=[]
        q=deque([root])
        flag=False
        while q:
            lvl=0
            for i in range(len(q)):
                node=q.popleft()
                lvl+=1
                if flag and(node.left or node.right):
                    return False
                if not node.left and not node.right:
                    flag=True
                if not node.left and node.right:
                    return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(lvl)
        for i in range(len(arr)-1):
            if arr[i]!=2**i:
                return False
        return True
