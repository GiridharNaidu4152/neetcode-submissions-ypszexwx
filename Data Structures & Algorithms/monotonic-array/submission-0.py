class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[1]>=nums[0]:
            increasing=True
        else:
            increasing=False

        for i in range(len(nums)-1):
            if increasing:
                if nums[i]>nums[i+1]:
                    return False
            else:
                if nums[i+1]>nums[i]:
                    return False
        return True