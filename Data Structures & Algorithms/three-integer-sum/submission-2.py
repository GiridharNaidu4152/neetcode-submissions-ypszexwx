class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        o=[]
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    result=sorted([nums[i],nums[l],nums[r]])
                    if result not in o:
                        o.append(result)
                    r-=1
                    l+=1
        return o



