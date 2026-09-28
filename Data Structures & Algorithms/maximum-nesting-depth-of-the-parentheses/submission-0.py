class Solution:
    def maxDepth(self, s: str) -> int:
        maxp=0
        parent=0
        for c in s:
            if maxp<parent:
                maxp=parent
            if c==")":
                parent-=1
            if c=="(":
                parent+=1
        return maxp