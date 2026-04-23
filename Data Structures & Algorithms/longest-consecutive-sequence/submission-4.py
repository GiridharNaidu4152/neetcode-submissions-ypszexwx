class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result=0
        for num in nums:
            current_num,streak=num,0
            while current_num in nums:
                current_num -=1
                streak+=1
            result=max(result,streak)
        return result