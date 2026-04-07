class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s.lower():
            if i in "qwertyuiopasdfghjklzxcvbnm1234567890":
                l.append(i)
        return l == l[::-1]