class Solution:
    def validPalindrome(self,s: str) -> bool:
        s1=list(s)
        if s1==s1[::-1] :
            return True
        else:
            for i in range(len(s1)):
                s2=s1[:i]+s1[i+1:]
                if s2==s2[::-1]:
                    return True
        return False
