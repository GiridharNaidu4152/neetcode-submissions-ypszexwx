class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)
        k%=s
        nums[:]=nums[s-k:s]+nums[:s-k]