class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        result=nums[:]
        result[0]=1
        b=1
        for i in range(1,len(nums)):
            result[i]=a*nums[i-1]
            a*=nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            result[i]=b*result[i]
            b*=nums[i]
        return result