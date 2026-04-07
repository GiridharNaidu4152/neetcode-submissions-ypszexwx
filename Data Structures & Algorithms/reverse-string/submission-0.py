class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a=s[:]
        b=len(s)
        for i in range(b):
            s[i]=a[b-i-1]
            