class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adic={}
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            b=tuple(count)
            if b not in adic:
                adic[b] = [s]
            else:
                adic[b].append(s)

        return list(adic.values())