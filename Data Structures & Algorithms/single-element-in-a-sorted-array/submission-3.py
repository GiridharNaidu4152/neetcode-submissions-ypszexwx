class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        while l<len(nums)-1:
            if nums[l]==nums[l+1]:
                l+=2
            else:
                return nums[l]
        return nums[-1]