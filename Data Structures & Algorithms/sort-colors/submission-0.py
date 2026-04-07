class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=True
        while flag:
            flag = False
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    flag=True
                    nums[i],nums[i+1]=nums[i+1],nums[i]