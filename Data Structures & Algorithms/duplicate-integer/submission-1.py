class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=list(set(nums))
        return len(a)!=len(nums)

    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.containsDuplicate(nums)