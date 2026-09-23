# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        goodnodes=0
        rootval=root.val
        q=deque([(root,float("-inf"))])
        while q:
            node,maxvalue=q.popleft()
            if node.val>=maxvalue:
                goodnodes+=1
            if node.right:
                q.append((node.right,max(maxvalue,node.val)))
            if node.left:
                q.append((node.left,max(maxvalue,node.val)))
        return goodnodes
