class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomdict={}
        for i in ransomNote:
            if i in ransomdict:
                ransomdict[i]+=1
            else:
                ransomdict[i]=1
        magdict={}
        for j in magazine:
            if j in magdict:
                magdict[j]+=1
            else:
                magdict[j]=1
        for a in ransomdict:
            if a in magdict:
                if ransomdict[a] > magdict[a]:
                    return False
            else:
                return False
        return True