class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(","]":"[","}":"{"}
        stk=[]
        for char in s:
            if char not in hashmap:
                stk.append(char)
            else:
                if stk and stk[-1]==hashmap[char]:
                    stk.pop()
                else:
                    return False
        return True if not stk else False