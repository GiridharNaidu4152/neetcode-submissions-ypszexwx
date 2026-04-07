class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr)==1:
                return arr
            m=len(arr)//2
            L=mergesort(arr[:m])
            R=mergesort(arr[m:])
            return merge(L,R)
    
        def merge(l,r):
            result=[]
            j,k=0,0
            while j<len(l) and k<len(r):
                if l[j]<=r[k]:
                    result.append(l[j])
                    j+=1
                else:
                    result.append(r[k])
                    k+=1
            while j<len(l):
                result.append(l[j])
                j+=1
            while k<len(r):
                result.append(r[k])
                k+=1
            return result
        return mergesort(nums)