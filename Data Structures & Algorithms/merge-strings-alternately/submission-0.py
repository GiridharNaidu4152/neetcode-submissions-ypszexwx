class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        minimum = min(len(word1),len(word2))
        for i in range(minimum*2):
            if i%2==0:
                result+=word1[i//2]
            if i%2==1:
                result+=word2[i//2]
        result+=word1[minimum:]+word2[minimum:]
        return result