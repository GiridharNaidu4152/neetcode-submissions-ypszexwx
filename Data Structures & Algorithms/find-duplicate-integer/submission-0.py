class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited=set()
        for c in nums:
            if c not in visited:
                visited.add(c)
            else :
                return c