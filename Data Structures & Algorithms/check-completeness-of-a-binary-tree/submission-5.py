# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        flag=False
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    if flag:
                        return False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    flag=True
        return True
